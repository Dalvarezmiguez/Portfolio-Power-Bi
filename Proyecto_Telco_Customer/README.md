# Análisis de Probabilidad de Abandono de Clientes – Telecomunicaciones (Python)

## Contexto
Dataset de **clientes de una compañía de Telecomunicaciones**, con información de perfil, servicios contratados, facturación y churn (bajas de clientes).  
Objetivo: predecir qué clientes tienen mayor probabilidad de darse de baja y analizar los factores que influyen en su abandono.

---

## Objetivos del análisis
- Explorar el dataset y detectar valores nulos o inconsistencias.  
- Limpiar y transformar las variables para modelado.  
- Entrenar modelos de **Machine Learning** (Logistic Regression, Random Forest, XGBoost) para predecir abandono.  
- Interpretar los factores más importantes que afectan a la baja de clientes.  
- Analizar el impacto del abandono sobre la cartera y la facturación.  
- Segmentar clientes según su **riesgo de abandono**.

---

## Estructura del análisis

1. **EDA en Python**
   - Limpieza de datos, detección de outliers y análisis descriptivo.  
   - Visualización de variables categóricas y numéricas.  
   - Proporción de género, tipo de contrato, servicios contratados y distribución de facturación.  

2. **Modelado**
   - Separación de variables independientes (`X`) y variable objetivo (`y`).  
   - Escalado de variables y codificación de categóricas.  
   - Entrenamiento de modelos: Logistic Regression, Random Forest, XGBoost.  
   - Evaluación de modelos: accuracy, ROC-AUC, matriz de confusión.  

3. **Interpretabilidad**
   - Importancia de variables con Random Forest.  
   - SHAP para XGBoost y análisis de contribución de cada variable.  

4. **Predicciones y análisis final**
   - Probabilidad de abandono (`Churn_Prob`) y predicción final (`Churn_Pred`).  
   - Impacto sobre la cartera y facturación.  
   - Segmentación de clientes según riesgo de abandono: bajo, medio o alto.

---

## Técnicas y herramientas
- **Python**: pandas, numpy, matplotlib, seaborn, scikit-learn, XGBoost, shap  
- **Machine Learning**: clasificación binaria (churn/no churn)  
- **Interpretabilidad**: feature importance y SHAP values  

---

## Dataset
- Fuente: **Kaggle**
- [Descargar dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)  

---

## Principales insights

- **Proporción de género**: la cartera está equilibrada con **3.488 mujeres y 3.555 hombres**.  
- **Predicción de abandono**:  
  - El **75,34 % de los clientes seguirán activos**, representando el **84,31 % de la facturación**.  
  - Las bajas afectan más en cantidad (**24,66 % de los clientes**), que en facturación (**15,69 % del total**).  
- **Riesgo de abandono**:  
  - El **65 % de los clientes tienen un riesgo bajo** de abandonar.  
  - Los clientes con **contrato mensual** tienen un **57,29 % de riesgo** de abandono.  
- **Variables más importantes para predecir abandono** (según Random Forest y SHAP):  
  - Tipo de contrato y duración del contrato.  
  - Facturación mensual y total.  
  - Servicios contratados: seguridad online, soporte técnico, streaming de TV/películas.  
  - Factura electrónica y presencia de líneas adicionales.

---

## Visualizaciones sugeridas
- **Distribución de género**: gráfico de barras comparando hombres y mujeres.  
- **Churn por tipo de contrato**: gráfico de columnas apiladas mostrando clientes que se quedan y se van.  
- **Top 10 variables importantes**: gráfico horizontal con Random Forest o SHAP.  
- **Segmentación de riesgo de abandono**: gráfico de pastel o barras con bajo/medio/alto riesgo.

---


## Dashboard – Ejemplo de visualizaciones

![Demo interactiva](https://dalvarezmiguez.github.io/img/Dashboard_Telco.gif)

Vista completa:  

**Página 1 – Predicción**  

![Resumen por año](https://dalvarezmiguez.github.io/img/prediccion.png)

**Página  – Detalle**  

![Resumen por año](https://dalvarezmiguez.github.io/img/detalle.png)

---

[Ver Proyecto →](../Proyecto_Telco_Customer/)