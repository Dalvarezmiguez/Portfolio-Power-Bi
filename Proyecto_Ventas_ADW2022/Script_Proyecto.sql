---DimProducto
SELECT 
    DISTINCT(p.ProductID)				AS IDProducto,       
    p.Name								AS Producto,        
    p.StandardCost							AS PrecioUnitario,
	CASE 
		WHEN CAST(SUM(i.Quantity) AS INT) IS NULL THEN 0
		ELSE CAST(SUM(i.Quantity) AS INT)
	END									AS Stock,  
    CAST(p.SafetyStockLevel AS INT)		AS StockSeguridad,
    CASE 
        WHEN c.Name IS NULL THEN 'Sin Categoria'
        ELSE c.Name
    END									AS Categoria,
    CASE
        WHEN s.Name IS NULL THEN 'Sin Categoria'
        ELSE s.Name
    END									AS Subcategoria
FROM Production.Product p
LEFT JOIN Production.ProductSubcategory s ON p.ProductSubcategoryID = s.ProductSubcategoryID
LEFT JOIN Production.ProductCategory c ON s.ProductCategoryID = c.ProductCategoryID
LEFT JOIN Production.ProductInventory i ON p.ProductID = i.ProductID
GROUP BY p.ProductID, p.Name, p.StandardCost, p.SafetyStockLevel, s.Name, c.Name;

---DimTerritorio
SELECT DISTINCT
    a.AddressID					AS IDDireccion,
    c.Name						AS País,
    sp.Name 					AS Provincia,
    st.Name 					AS Territorio,
    st.TerritoryID				AS IDTerritorio
FROM Person.BusinessEntityAddress b
LEFT JOIN Person.Address a ON b.AddressID = a.AddressID
LEFT JOIN Person.StateProvince sp ON a.StateProvinceID = sp.StateProvinceID
LEFT JOIN Person.CountryRegion c ON sp.CountryRegionCode = c.CountryRegionCode
LEFT JOIN Sales.SalesTerritory st ON sp.TerritoryID = st.TerritoryID;

---DimClientes
SELECT DISTINCT
    c.CustomerID														AS IDCliente,
    CONCAT(COALESCE(p.FirstName, ''), ' ', COALESCE(p.LastName, ''))	AS Nombre,
    e.EmailAddress														AS Email,
    ph.PhoneNumber														AS Teléfono,
    pt.Name																AS TipoTeléfono
FROM Person.Person p
LEFT JOIN Sales.Customer c ON p.BusinessEntityID = c.PersonID
LEFT JOIN Person.EmailAddress e ON p.BusinessEntityID = e.BusinessEntityID
LEFT JOIN Person.PersonPhone ph ON p.BusinessEntityID = ph.BusinessEntityID
LEFT JOIN Person.PhoneNumberType pt ON ph.PhoneNumberTypeID = pt.PhoneNumberTypeID
JOIN Sales.Store s ON c.StoreID = s.BusinessEntityID
LEFT JOIN Person.BusinessEntityContact sc ON s.BusinessEntityID = sc.BusinessEntityID
LEFT JOIN Person.ContactType ct ON sc.ContactTypeID = ct.ContactTypeID;

---DimClientesTiendas
SELECT DISTINCT  
    s.BusinessEntityID		AS IDTienda,
    s.Name					AS Empresa,
    s.SalesPersonID			AS IDComercial
FROM Sales.Store s;

---DimContactoTiendas
SELECT
	s.BusinessEntityID									AS IDTienda,
	p.FirstName + ' ' + p.LastName						AS Nombre,
	ea.EmailAddress										AS Email,
	ph.PhoneNumber										AS Telefono,
	pt.Name												AS TipoTelefono,
	ct.Name												AS Puesto,
	s.SalesPersonID										AS IDComercial
FROM Sales.Store s
JOIN Sales.Customer c ON s.BusinessEntityID = c.CustomerID
JOIN Person.BusinessEntity be ON s.BusinessEntityID = be.BusinessEntityID
JOIN Person.BusinessEntityContact bec ON be.BusinessEntityID = bec.BusinessEntityID
JOIN Person.Person p ON bec.PersonID = p.BusinessEntityID
JOIN Person.ContactType ct ON bec.ContactTypeID = ct.ContactTypeID
LEFT JOIN Person.EmailAddress ea ON p.BusinessEntityID = ea.BusinessEntityID
LEFT JOIN Person.PersonPhone ph ON p.BusinessEntityID = ph.BusinessEntityID
LEFT JOIN Person.PhoneNumberType pt ON ph.PhoneNumberTypeID = pt.PhoneNumberTypeID;

---DimComerciales
SELECT DISTINCT
    CASE 
        WHEN soh.SalesPersonID IS NULL THEN 0
        ELSE soh.SalesPersonID
    END																			AS IDComercial,
    CAST(CASE 
        WHEN sp.TerritoryID IS NULL THEN 0
        ELSE sp.TerritoryID
    END AS INT)																	AS IDTerritorio,
    CASE 
        WHEN st.[Group] IS NULL THEN 'Sin Territorio Asignado'
        ELSE st.[Group]
    END																			AS Territorio,
    CASE
        WHEN p.FirstName IS NULL THEN 'Ventas sin Comercial'
        ELSE CONCAT(COALESCE(p.FirstName, ''), ' ', COALESCE(p.LastName, ''))
    END																			AS Nombre,
	CASE
        WHEN e.EmailAddress IS NULL THEN 'Sin Email Asignado'
        ELSE e.EmailAddress
    END																			AS Email,
	CASE
        WHEN ph.PhoneNumber IS NULL THEN 'Sin Teléfono Asignado'
        ELSE ph.PhoneNumber
    END																			AS Teléfono,
	CASE
        WHEN pt.Name IS NULL THEN 'Sin Tipo Asignado'
        ELSE pt.Name
    END																			AS TipoTeléfono
FROM Sales.SalesOrderHeader soh
LEFT JOIN Sales.SalesPerson sp ON soh.SalesPersonID = sp.BusinessEntityID
LEFT JOIN Person.Person p ON sp.BusinessEntityID = p.BusinessEntityID
LEFT JOIN Person.EmailAddress e ON p.BusinessEntityID = e.BusinessEntityID
LEFT JOIN Person.PersonPhone ph ON p.BusinessEntityID = ph.BusinessEntityID
LEFT JOIN Person.PhoneNumberType pt ON ph.PhoneNumberTypeID = pt.PhoneNumberTypeID
LEFT JOIN Sales.SalesTerritory st ON sp.TerritoryID = st.TerritoryID;

---DimObjetivosComerciales
SELECT
	BusinessEntityID	AS IDComercial,
	SalesQuota			AS Objetivos,
	QuotaDate			AS FechaObjetivos
FROM Sales.SalesPersonQuotaHistory

---FactVentas
SELECT DISTINCT
    soh.SalesOrderID AS IDPedido,
    CAST(soh.OrderDate AS DATE)						AS FechaPedido,
    soh.OnlineOrderFlag								AS VentaOnline,
    soh.SalesOrderNumber							AS NumeroPedido,
    soh.CustomerID									AS IDCliente,
    CAST(CASE 
        WHEN soh.SalesPersonID IS NULL THEN 0
        ELSE soh.SalesPersonID
    END AS INT)										AS IDComercial,
    soh.BillToAddressID AS IDDireccionFacturacion,
    c.StoreID										AS IDTienda,
    CAST(CASE 
        WHEN sp.TerritoryID IS NULL THEN 0
        ELSE sp.TerritoryID
    END AS INT)										AS IDTerritorio,
    sod.OrderQty									AS Cantidad,
    sod.ProductID									AS IDProducto,
    sod.UnitPrice									AS PrecioUnitario,
    CASE 
        WHEN soh.OnlineOrderFlag = 1 THEN 'Online'
        ELSE 'Offline'
    END												AS Canal
FROM Sales.SalesOrderDetail sod
LEFT JOIN Sales.SalesOrderHeader soh ON sod.SalesOrderID = soh.SalesOrderID
LEFT JOIN Sales.Customer c ON soh.CustomerID = c.CustomerID
LEFT JOIN Person.Address a ON soh.BillToAddressID = a.AddressID
LEFT JOIN Sales.SalesPerson sp ON soh.SalesPersonID = sp.BusinessEntityID;


