---DimProducto
SELECT
    p.ProductID						AS IDProducto,
    p.Name							AS NombreProducto,
    SUM(pi.Quantity)				AS Stock,
    CASE 
        WHEN pc.Name IS NULL THEN 'Sin Categorizar'
        ELSE pc.Name
    END AS Categoria,
    CASE
        WHEN psc.Name IS NULL THEN 'Sin Categorizar'
        ELSE psc.Name
    END AS Subcategoria
FROM Production.Product p
LEFT JOIN Production.ProductSubcategory psc ON p.ProductSubcategoryID = psc.ProductSubcategoryID
LEFT JOIN Production.ProductCategory pc ON psc.ProductCategoryID = pc.ProductCategoryID
LEFT JOIN Production.ProductInventory pi ON p.ProductID = pi.ProductID
GROUP BY p.ProductID, p.Name, pc.Name, psc.Name

---DimProveedor
SELECT DISTINCT
    v.BusinessEntityID										AS IDProveedor,
    v.Name													AS NombreProveedor,
    a.StateProvinceID										AS IDProvincia,
    p.ProductID												AS IDProducto,
    CAST(CONCAT(p.ProductID, v.BusinessEntityID) AS INT)	AS IDProductoProveedor,
    pv.AverageLeadTime										AS TiempoMedioEnvio,
    pv.StandardPrice										AS PrecioCosteActual,
    pv.LastReceiptCost										AS PrecioCosteAnterior,
    pv.MinOrderQty											AS CantidadMinimaPedido,
    pv.MaxOrderQty											AS CantidadMaximaPedido
FROM Purchasing.Vendor v
INNER JOIN Purchasing.ProductVendor pv ON v.BusinessEntityID = pv.BusinessEntityID
INNER JOIN Production.Product p ON pv.ProductID = p.ProductID
LEFT JOIN Person.BusinessEntity be ON v.BusinessEntityID = be.BusinessEntityID
LEFT JOIN Person.BusinessEntityAddress ea ON be.BusinessEntityID= ea.BusinessEntityID
LEFT JOIN Person.Address a ON ea.AddressID = a.AddressID

---DimTerritorio
SELECT DISTINCT
    a.StateProvinceID	AS IDProvincia,
    c.Name				AS Pais,
    s.Name				AS Provincia
FROM Person.BusinessEntityAddress b
LEFT JOIN Person.Address a ON b.AddressID = a.AddressID
LEFT JOIN Person.StateProvince s ON a.StateProvinceID = s.StateProvinceID
LEFT JOIN Person.CountryRegion c ON s.CountryRegionCode = c.CountryRegionCode

---FactCompras
SELECT 
    poh.PurchaseOrderID							AS IDCompra,
    poh.OrderDate								AS FechaCompra,
    poh.Status                                  AS Estado,
    poh.VendorID								AS IDProveedor,
    pod.OrderQty								AS CantidadComprada,
    pod.ProductID								AS IDProducto,
	poh.ShipMethodID							AS IDModoenvio,
	poh.ShipDate								AS FechaEnvio,
	poh.SubTotal								AS SubTotal,
	poh.TaxAmt									AS Tasas,
	poh.Freight									AS CosteEnvio,
	poh.Totaldue								AS TotalPedido,
	pod.DueDate									AS FechaEntrega,
	pod.UnitPrice								AS PrecioUnitario,
	pod.LineTotal								AS CosteTotal,
	pod.ReceivedQty								AS CantidadRecibida,
	pod.RejectedQty								AS CantidadRechazada,
	pod.StockedQty								AS CantidadStockada,
	CONCAT(pod.ProductID,poh.VendorID)			AS IDProductoProveedor,
	CAST(pod.DueDate - poh.OrderDate AS INT)	AS FechaEntregaReal
FROM AdventureWorks2022.Purchasing.PurchaseOrderHeader poh
LEFT JOIN AdventureWorks2022.Purchasing.PurchaseOrderDetail pod ON poh.PurchaseOrderID = pod.PurchaseOrderID

---FactVentas
SELECT DISTINCT
    soh.SalesOrderID				AS IDPedido,
    soh.OrderDate					AS FechaVenta,
    sod.ProductID					AS IDProducto,
    v.BusinessEntityID				AS IDProveedor,
    soh.BillToAddressID				AS IDDireccionFacturacion,  
    sod.OrderQty					AS CantidadVendida,
    sod.UnitPrice					AS PrecioUnitario,
    a.StateProvinceID				AS IDProvincia
FROM AdventureWorks2022.Sales.SalesOrderHeader soh  
LEFT JOIN Sales.SalesOrderDetail sod ON soh.SalesOrderID = sod.SalesOrderID
LEFT JOIN Purchasing.ProductVendor v ON sod.ProductID = v.ProductID
LEFT JOIN Person.Address a ON soh.BillToAddressID = a.AddressID
