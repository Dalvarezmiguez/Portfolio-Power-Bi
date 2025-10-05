# Análisis de Ventas - Power BI + SQL

## Contexto
Dataset de ventas de retail, incluyendo información de productos, comerciales, canales y registros históricos.
Objetivo: generar insights accionables para decisiones comerciales estratégicas y realizar proyecciones de ventas.

---

## Objetivos del análisis
- Analizar la evolución de ventas y márgenes por producto y categoría.
- Evaluar la performance por canal de venta.
- Analizar la contribución de cada comercial y su cartera.
- Realizar proyecciones de ventas basadas en histórico.

---

## Estructura del Dashboard

1. **Ventas generales**
- KPIs: ventas totales, margen, productos top.
- Gráficos de evolución mensual y por categoría.

2. **Ventas por canal**
- Comparativa entre canales (online, tiendas físicas, distribuidores).
- Identificación de canales más rentables.

3. **Ventas por comercial**
- Ranking de comerciales según ventas y margen.
- Identificación de comerciales estratégicos y su cartera.

4. **Proyección de ventas**
- Forecast basado en histórico.
- Gráficos de tendencias y predicciones para el próximo trimestre.

---

## Técnicas y herramientas
- **Power BI**: dashboards interactivos, segmentaciones y KPIs.
- **SQL**: extracción de datos, JOINs y agregaciones.
- **DAX**: medidas para cálculos de margen, crecimiento y proyecciones.
- **Power Query**: limpieza y transformación de datos.

---

## Dataset
- Fuente: **AdventureWorks 2022** (SQL Server sample database)
- [Más información y descarga](https://github.com/Microsoft/sql-server-samples/releases/tag/adventureworks)

---

## Principales insights
- El 20% de los productos genera el 60% de las ventas.
- Canal online crece a más del doble del ritmo que el offline.
- Cuatro comerciales concentran más del 50% de la cartera de clientes.
- Según las proyecciones la empresa cuenta con stock suficiente para las ventas de las próximas 4 semanas.

---

## Dashboard – Ejemplo de visualizaciones

![Demo interactiva](https://dalvarezmiguez.github.io/img/Dashboard_Ventas.gif)

Vista completa:  

**Marcador 1 – Informe Resumen**

![Informe Resumen](https://dalvarezmiguez.github.io/img/informe_resumen.png)

**Marcador 2 – Detalle Por Canal**

![Detalle Por Canal](https://dalvarezmiguez.github.io/img/detalle_por_canal.png)

**Marcador 3 – Detalle Comerciales**

![Detalle Comerciales](https://dalvarezmiguez.github.io/img/detalle_comerciales.png)

**Marcador 4 – Proyección Ventas**

![Proyección Ventas](https://dalvarezmiguez.github.io/img/proyeccion_ventas.png)

**Marcador 5 – Detalle Ventas**

![Proyección Ventas](https://dalvarezmiguez.github.io/img/detalle_ventas_diarias.png)

[Ver Proyecto →](../Proyecto_Ventas_ADW2022/)