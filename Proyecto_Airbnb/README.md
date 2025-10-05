# Análisis de Airbnb – Madrid (Python + Power BI)

## Contexto
Dataset de alojamientos de **Airbnb en Madrid**, con información de viviendas, anfitriones y reseñas.  
Objetivo: analizar la oferta turística, precios, licencias y concentración de anfitriones para obtener insights sobre el mercado.

---

## Objetivos del análisis
- Analizar la distribución de tipos de alojamiento (pisos enteros, habitaciones privadas, etc.).  
- Evaluar la concentración de propiedades por anfitrión.  
- Identificar patrones de precios medios en función del tipo de alojamiento.  
- Explorar la relación entre número de reseñas y precios.  
- Detectar el nivel de viviendas con licencia.  

---

## Estructura del análisis

1. **EDA en Python**
- Limpieza de datos, detección de outliers y análisis descriptivo.  
- Estadísticos básicos y visualizaciones exploratorias (distribución de precios, densidad por barrios, etc.).  

2. **Dashboard en Power BI**
- **Viviendas** → KPIs: total viviendas, precio medio, % con licencia, distribución por tipo.  
- **Anfitriones** → ranking de anfitriones y concentración de propiedades.  
- **Reseñas** → análisis de reseñas por barrio y relación con precios.  

---

## Técnicas y herramientas
- **Python**: EDA, limpieza y transformación de datos (pandas, numpy, matplotlib, seaborn).  
- **Power BI**: dashboards interactivos, segmentaciones y KPIs.  
- **Power Query**: integración y modelado de datos en Power BI.  

---

## Dataset
- Fuente: **Inside Airbnb** (open data)  
- [Descargar dataset](https://insideairbnb.com/get-the-data/?utm_source)  

---

## Principales insights
- El **68,29 %** de los alquileres corresponde a **pisos enteros**.  
- El **precio medio** de un piso completo es de **126,97 €**, mientras que el de una habitación de hotel en Airbnb asciende a **140,60 €**.  
- El **número de reseñas no está correlacionado con el precio**.  
- En Madrid existen **18.792 pisos**, con un precio medio de **104,85 €**.  
- El **80,79 % de las viviendas no cuentan con licencia**.  

---

## Dashboard – Ejemplo de visualizaciones

![Demo interactiva](https://dalvarezmiguez.github.io/img/Dashboard_Airbnb.gif)

Vista completa:

**Página 1 – Viviendas**  
![Viviendas](https://dalvarezmiguez.github.io/img/viviendas.png)

**Página 2 – Anfitriones**  
![Anfitriones](https://dalvarezmiguez.github.io/img/anfitriones.png)

**Página 3 – Reseñas**  
![Reseñas](https://dalvarezmiguez.github.io/img/reseñas.png)

[Ver Proyecto →](../Proyecto_Airbnb)

---
