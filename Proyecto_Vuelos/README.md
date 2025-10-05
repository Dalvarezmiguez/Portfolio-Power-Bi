# Análisis de Retrasos y Cancelaciones de Vuelos – Proyecto Vuelos (R y Tableau)

## Contexto
Dataset de **vuelos comerciales en 2024**, con información de aerolíneas, aeropuertos, retrasos, cancelaciones y motivos asociados.  
Objetivo: analizar los patrones de retrasos y cancelaciones, identificar aerolíneas y aeropuertos más afectados y explorar factores que impactan la eficiencia de los vuelos.

---

## Objetivos del análisis
- Limpiar y transformar un dataset de **más de 7 millones de filas** utilizando **R** y `fread` para mayor rapidez.  
- Analizar los retrasos y cancelaciones por aerolínea, aeropuerto y mes.  
- Identificar causas principales de cancelaciones y retrasos.  
- Evaluar la eficiencia de aeropuertos y aerolíneas.  
- Visualizar los insights en un **dashboard interactivo** en Tableau.

---

## Estructura del análisis

1. **Limpieza y transformación de datos en R**
   - Lectura rápida del dataset con `fread` de **data.table**.  
   - Tratamiento de valores nulos e inconsistencias.  
   - Creación de variables agregadas para análisis de cancelaciones y retrasos.  

2. **Análisis descriptivo**
   - Distribución de vuelos por aerolínea y aeropuerto.  
   - Retrasos según motivo (compañía, avión, meteorología).  
   - Cancelaciones totales y tasas de cancelación por aerolínea.  

3. **Visualización y dashboard**
   - Tableau Cloud para crear un dashboard interactivo.  
   - Segmentación por mes, aerolínea y aeropuerto.  
   - Gráficos de barras, líneas y mapas para representar retrasos y cancelaciones.

---

## Técnicas y herramientas
- **R**: data.table (`fread`), dplyr, ggplot2  
- **Visualización**: Tableau  
- **Análisis**: agregación por aerolínea, aeropuerto, motivo y mes

---

## Dataset
- Fuente: **Kaggle**  
- [Descargar dataset](https://www.kaggle.com/datasets/hrishitpatil/flight-data-2024)

---

## Principales insights

- **Cancelaciones por aerolínea**  
  - **American Airlines** lidera en número de vuelos cancelados con **15.050 vuelos**.  
  - **Frontier Airlines** tiene la mayor **tasa de cancelación** con **2,32 %**.  

- **Vuelos y retrasos**  
  - **Southwest Airlines**, aerolínea de bajo coste, tiene más vuelos en todo el año (**1.419.419 vuelos**) y es la compañía con más retrasos (**199.913 por motivos de avión, 169.751 por motivos de compañía**).  

- **Eficiencia aeroportuaria**  
  - El **aeropuerto de Texas** registra más retrasos sin embargo cuenta con buenos datos en tiempo medio de los aviones en pista tanto en salidas como llegadas.

- **Causas de cancelación**  
  - El **55,48 % de las cancelaciones** se producen por causas meteorológicas.

---

## Visualizaciones sugeridas
- **Vuelos y cancelaciones por aerolínea**: gráfico de barras comparativo.  
- **Retrasos por motivo**: gráfico apilado por avión, compañía y meteorología.  
- **Eficiencia de aeropuertos**: gráfico de burbujas con tiempo medio en pista y gráfico de barras apiladas con retrasos totales.  
- **Tendencia mensual de vuelos**: gráfico de líneas por mes.

---

## Dashboard – Tableau Cloud
[Acceder al dashboard interactivo](https://public.tableau.com/views/Proyecto_Vuelos_17594980949080/Informe?:language=es-ES&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Dashboard – Ejemplo de visualizaciones

![Demo interactiva](https://dalvarezmiguez.github.io/img/dashboard_aviones.gif)

Vista completa:  

**Página 1 – Informe**  

![Resumen por año](https://dalvarezmiguez.github.io/img/proyecto_aviones.png)