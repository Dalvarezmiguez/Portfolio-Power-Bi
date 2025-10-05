# Análisis de Compras - Power BI + SQL

## Contexto
Dataset de compras a proveedores, incluyendo información de productos, proveedores y cantidades adquiridas.
Objetivo: mejorar la eficiencia en la gestión de proveedores, optimizar stock y controlar costes de manera estratégica.

---

## Objetivos del análisis
- Identificar proveedores más importantes según volumen, fiabilidad y gasto.
- Analizar patrones de compras por categoría de producto.
- Detectar oportunidades de ahorro y optimización de stock.
- Evaluar tendencias históricas de compras para mejorar planificación.

---

## Estructura del Dashboard

1. **Compras generales**
- KPIs: gasto total, volumen de productos, categorías más compradas.
- Gráficos de evolución mensual y por categoría de producto.

2. **Compras por proveedor**
- Ranking de proveedores según volumen y costo total.
- Identificación de proveedores estratégicos y críticos.

3. **Análisis por categoría de producto**
- Distribución del gasto por categorías.
- Productos con mayor gasto y frecuencia de compra.

---

## Técnicas y herramientas
- **Power BI**: dashboards interactivos, segmentaciones y KPIs.
- **DAX**: medidas para cálculos de gasto total, promedio por proveedor y porcentaje de contribución.
- **Power Query**: limpieza y transformación de datos.
- **SQL**: extracción de datos con JOINs y agregaciones.

---

## Dataset
- Fuente: **AdventureWorks 2022** (SQL Server sample database)
- [Más información y descarga](https://github.com/Microsoft/sql-server-samples/releases/tag/adventureworks)

---

## Principales insights
- Tres proveedores concentran más del 50% del gasto total.
- Es necesario optimizar las compras y trabajar en la eficiencia del stock.
- Identificación de oportunidades de consolidación de proveedores para optimizar costos.
- En Europa se realizan ventas y no tenemos proveedores locales.

---

## Dashboard – Ejemplo de visualizaciones

![Demo interactiva](https://dalvarezmiguez.github.io/img/Dashboard_Compras.gif)

Vista completa:  

**Página 1 – Informe**

![Informe](https://dalvarezmiguez.github.io/img/informe.png)

**Marcador 1 – Detalle Pedidos**

![Detalle Pedidos](https://dalvarezmiguez.github.io/img/detalle_pedidos.png)

**Marcador 2 – Detalle Productos**

![Detalle Productos](https://dalvarezmiguez.github.io/img/detalle_productos.png)

**Marcador 3 – Detalle Proveedores**

![Detalle Proveedores](https://dalvarezmiguez.github.io/img/detalle_proveedores.png)

[Ver Proyecto →](../Proyecto_Compras_ADW2022/)