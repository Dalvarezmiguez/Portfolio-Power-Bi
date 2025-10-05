# Análisis del Presupuesto de la Generalitat de Catalunya (1999–2023) – Power BI

## Contexto
Dataset con información histórica de los **presupuestos de la Generalitat de Catalunya** desde **1999 hasta 2023** (con ausencia de datos en 2013, 2016, 2018, 2019 y 2021).  
Objetivo: analizar y comparar la evolución de **ingresos y gastos**, identificar principales variaciones y evaluar la estructura presupuestaria mediante un **dashboard interactivo en Power BI**.

---

## Objetivos del análisis
- Analizar la evolución histórica de ingresos y gastos públicos.  
- Identificar variaciones interanuales (absolutas y porcentuales).  
- Evaluar la composición del gasto (personal, capital, transferencias, etc.).  
- Medir la dependencia de transferencias corrientes y su impacto en la sostenibilidad presupuestaria.  

---

## Estructura del Dashboard

1. **Resumen financiero**
   - KPIs: ingresos totales, gastos totales, variación interanual.
   - Gráficos de líneas y barras para evolución temporal.

2. **Ingresos**
   - Gráfico circular/anillos para distribución por tipo de ingreso.  
   - Evolución de impuestos directos, indirectos y transferencias.  

3. **Gastos**
   - Treemap y gráficos de cintas mostrando reparto del gasto.  
   - Evolución de gastos de personal, transferencias e inversión en infraestructuras.  

4. **Comparativa interanual**
   - Matriz con diferencias absolutas y porcentuales.  
   - KPI de crecimiento YoY.  

---

## Técnicas y herramientas
- **Power BI**: dashboard interactivo con segmentaciones por año y tipo de operación.  
- **DAX**: medidas de gastos e ingresos, diferencias interanuales y time intelligence.  
- **Power Query**: limpieza, normalización, combinación de tablas y creación de métricas de variación.  
- **Datos abiertos**: extracción desde portal oficial Idescat.  

---

## Dataset
- Fuente: [Idescat – Presupuestos de la Generalitat de Catalunya](https://www.idescat.cat/indicadors/?id=aec&lang=es&n=15638&utm_source)  
- Formatos: **tabular y plano**.  
- Procesados en **Power Query** (transformación y modelado).  

---

## Principales insights
- Los **ingresos crecieron un +5,7%** respecto a 2022, impulsados por impuestos directos e indirectos.  
- Los **gastos de personal aumentaron un +11,8%**, reflejando un mayor esfuerzo en recursos humanos.  
- Las **transferencias de capital cayeron un -33,6%**, reduciendo la inversión en infraestructuras.  
- La **dependencia de transferencias corrientes** sigue siendo elevada (≈48% del gasto total).  

---

## Valor añadido del proyecto
- Ejercicio completo de **ETL en Power Query** con múltiples formatos de datos.  
- Desarrollo de un **dashboard financiero interactivo** basado en datos públicos reales.  
- Proyecto enfocado en **transparencia y gestión pública**, con aplicación directa en análisis gubernamental.  
- Caso sólido para portfolio en **Data Analytics & Business Intelligence**.  

---

## Dashboard – Ejemplo de visualizaciones

![Demo interactiva](https://dalvarezmiguez.github.io/img/Dashboard_Cataluña.gif)

Vista completa:  

**Página 1 – Resumen financiero**  

![Cataluña](https://dalvarezmiguez.github.io/img/cataluña.png)

[Ver Proyecto →](../Proyecto_Cataluña/)