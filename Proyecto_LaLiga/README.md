# Análisis de LaLiga - Power BI

## Contexto
Dataset de las clasificaciones históricas de LaLiga, la primera división española, incluyendo información de los últimos 10 años (contando la temporada actual).  
Los datos se obtienen desde [Transfermarkt](https://www.transfermarkt.es/).  
Objetivo: analizar la evolución de los equipos, sus puntos, goles y posiciones para obtener insights sobre rendimiento histórico y tendencias.

---

## Objetivos del análisis
- Analizar la clasificación histórica de los últimos 10 años en términos de puntos, goles y posición media.  
- Identificar los equipos más consistentes y los más irregulares.  
- Evaluar el rendimiento de los máximos goleadores y los equipos menos goleados.  
- Facilitar la visualización de las clasificaciones anuales y la comparación entre temporadas.

---

## Estructura del Dashboard

1. **Resumen por año**
- Filtro por temporada.  
- Visualiza el escudo del campeón, el máximo goleador, el equipo menos goleado y los 3 descendidos.  

2. **Clasificación histórica por puntos**
- Suma de todos los indicadores de los últimos 10 años.  
- Tooltip con gráfico de líneas mostrando la evolución del total de puntos por año.  

3. **Clasificación histórica por posición media**
- Calcula la posición media, goles a favor, goles en contra y puntos promedio en los últimos 10 años.  
- Tooltip con la posición de cada equipo año por año.  

4. **Tabla de clasificaciones anuales**
- Permite filtrar por temporada y ver la clasificación final de cualquier año, incluyendo la actual.

---

## Técnicas y herramientas
- **Power BI**: dashboards interactivos con filtros y tooltips.  
- **DAX**: medidas para cálculos de puntos totales, promedio de goles y posición media.  
- **Power Query**: limpieza y transformación de datos.  

---

## Dataset
- Fuente: [Transfermarkt - LaLiga](https://www.transfermarkt.es/)  
- Incluye clasificaciones, goles a favor, goles en contra, puntos y posiciones de los últimos 10 años.

---

## Principales insights
- **Barcelona** lidera ambas clasificaciones históricas, con 12 puntos por encima del Real Madrid y una diferencia de 0,11 en posición media.
- El Villarreal es el equipo menos goleado en la última década, a pesar de no figurar entre los tres primeros en palmarés. 
- Las posiciones de la clasificación histórica por puntos y por posición media no siempre coinciden, mostrando la irregularidad de algunos equipos.  
- Equipos como **Sporting** o **Málaga, Almería, Deportivo y Huesca** solo han estado 1 y 2 temporadas en primera división en la última década.  
- La evolución de puntos y posiciones permite identificar equipos consistentes frente a equipos con rendimientos fluctuantes.

---

## Dashboard – Ejemplo de visualizaciones

![Demo interactiva](https://dalvarezmiguez.github.io/img/Dashboard_LaLiga.gif)

Vista completa:  

**Página 1 – Palmarés**  

![Resumen por año](https://dalvarezmiguez.github.io/img/palmares.png)

**Página  – Resumen por año**  

![Resumen por año](https://dalvarezmiguez.github.io/img/resumen_por_año.png)

**Página 3 – Clasificación histórica por puntos**  

![Histórica puntos](https://dalvarezmiguez.github.io/img/historica_por_puntos.png)

**Página 4 – Clasificación histórica por posición media**  

![Histórica posición media](https://dalvarezmiguez.github.io/img/historica_por_posicion_media.png)

**Página 5 – Clasificación anual filtrable**  

![Clasificación anual](https://dalvarezmiguez.github.io/img/clasificacion_anual.png)

[Ver Proyecto →](../Proyecto_LaLiga/)