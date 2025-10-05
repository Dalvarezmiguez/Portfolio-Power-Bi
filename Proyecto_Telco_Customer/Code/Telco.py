# %% [markdown]
# # 1.Carga y exploración inicial datos

# %%
# ======================
# 1.1 Importar Librerías
# ======================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
import shap

# %%
# ==============================================================
# 1.2 Cargar dataset (ajusta la ruta)
# ==============================================================
import os
from pathlib import Path
import platform
import pandas as pd

# Detectar sistema operativo
so = platform.system()  # Devuelve 'Windows', 'Darwin' (Mac) o 'Linux'

if so == "Windows":
    project_dir = Path(r"D:\Cursos\Data_Analytics\Portfolio\Portfolio_Github\Proyecto_Telco_Customer")
elif so == "Darwin":  # Mac
    project_dir = Path("/Users/danielalvarezmiguez/Desktop/Portfolio-Power-Bi/Proyecto_Telco_Customer")
else:
    raise Exception("Sistema operativo no soportado")

# Ruta al CSV dentro de Data
csv_path = project_dir / "Data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"

# Verifica que exista
print("Ruta CSV:", csv_path)
print("Existe?", csv_path.exists())

# Leer CSV
if csv_path.exists():
    df = pd.read_csv(csv_path)
else:
    raise FileNotFoundError(f"No se encontró el archivo CSV en {csv_path}")

# %%
# ==============================================================
# 1.3 Ver número filas y columnas
# ==============================================================
print("Dimensiones del dataset:", df.shape)

# %%
# ==============================================================
# 1.4 Ver primeras filas
# ==============================================================
print(df.head(20).to_string())

# %%
# ==============================================================
# 1.5 Ver tipos de datos
# ==============================================================
print(df.info())

# %%
# ==============================================================
# 1.6 Ver valores nulos por columna
# ==============================================================
# Total de filas
total_filas = len(df)

# Conteo de nulos
nulos = df.isnull().sum()

# Porcentaje de nulos
porcentaje_nulos = (nulos / total_filas) * 100

# Mostrar como DataFrame ordenado
resultado = pd.DataFrame({
    'Nulos': nulos,
    'Porcentaje (%)': porcentaje_nulos.round(2)
}).sort_values(by='Porcentaje (%)', ascending=False)

print(resultado)

# %% [markdown]
# # 2.Limpieza de datos

# %%
# ==============================================================
# 2.1 Pasar TotalCharges a numérico (tiene espacios vacíos)
# ==============================================================
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

# %%
# ==============================================================
# 2.2 Eliminar customerID
# ==============================================================
# Guardamos customerID antes de eliminarlo
customer_ids = df["customerID"].copy()  # copia de la columna original

# Ahora podemos eliminar la columna para ML
df.drop("customerID", axis=1, inplace=True)

# %%
# ==============================================================
# 2.3 Renombrar columnas
# ==============================================================
df.rename(columns={
    "gender": "Género",
    "SeniorCitizen": "Adulto_Mayor",
    "Partner": "Pareja",
    "Dependents": "Dependientes",
    "tenure": "Meses_Contrato",
    "PhoneService": "Servicio_Teléfono",
    "MultipleLines": "Lineas_Adicionales",
    "InternetService": "Servicio_Internet",
    "OnlineSecurity": "Seguridad_Online",
    "OnlineBackup": "Backup_Online",
    "DeviceProtection": "Protección_Dispositivo",
    "TechSupport": "Soporte_Técnico",
    "StreamingTV": "Streaming_TV",
    "StreamingMovies": "Streaming_Películas",
    "Contract": "Tipo_Contrato",
    "PaperlessBilling": "Factura_Electrónica",
    "PaymentMethod": "Método_Pago",
    "MonthlyCharges": "Cobro_Mensual",
    "TotalCharges": "Cobro_Total",
    "Churn": "Cliente_Baja"
}, inplace=True)


# %%
# ==============================================================
# 2.4 Ver valores únicos en las columnas
# ==============================================================
columnas = [
    "Género", "Adulto_Mayor", "Pareja", "Dependientes", "Servicio_Teléfono",
    "Lineas_Adicionales", "Servicio_Internet", "Seguridad_Online",
    "Backup_Online", "Protección_Dispositivo", "Soporte_Técnico",
    "Streaming_TV", "Streaming_Películas", "Tipo_Contrato",
    "Factura_Electrónica", "Método_Pago", "Cliente_Baja"
]

for col in columnas:
    valores = df[col].unique().tolist()
    print(f"\n--- {col} ---")
    # si hay más de 20 valores, solo mostramos los primeros
    if len(valores) > 20:
        print(valores[:20], "...")  
        print(f"(Total de valores únicos: {len(valores)})")
    else:
        print(valores)


# %%
# ==============================================================
# 2.5 Convertir variables categóricas
# ==============================================================
# Columnas categóricas binarias
cat_cols_bin = [col for col in df.select_dtypes(include=["object"]).columns if df[col].nunique() == 2]

# Guardamos encoders para revertir
encoders = {}

for col in cat_cols_bin:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Columnas categóricas con más de 2 categorías
cat_cols_multi = [col for col in df.select_dtypes(include=["object"]).columns if df[col].nunique() > 2]

# Creamos un dataframe temporal con dummies
df_dummies = pd.get_dummies(df[cat_cols_multi], drop_first=True)

# Concatenamos las columnas dummy al dataframe original y eliminamos las originales de categoría múltiple
df = pd.concat([df.drop(columns=cat_cols_multi), df_dummies], axis=1)

# %%
# ==============================================================
# 2.6 Reemplaza espacios, guiones y palabras en inglés
# ==============================================================
df.columns = [c.replace(" ", "_").replace("-", "_")
              .replace("No_internet_service", "Sin_Internet")
              .replace("Fiber_optic", "Fibra")
              .replace("Yes", "Si") for c in df.columns]

# Guardar columnas finales en español
columnas = df.drop("Cliente_Baja", axis=1).columns

# %% [markdown]
# # 3. Separar X / Y

# %%
# ==============================================================
# 3. Separar X / Y
# ==============================================================
X = df.drop("Cliente_Baja", axis=1)
y = df["Cliente_Baja"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

# %% [markdown]
# # 4. Modelos

# %%
# ==============================================================
# 4.1 Logistic Regression
# ==============================================================
log_reg = LogisticRegression(max_iter=500)
log_reg.fit(X_train, y_train)
y_pred_lr = log_reg.predict(X_test)

print("Logistic Regression")
print(classification_report(y_test, y_pred_lr))
print("ROC-AUC:", roc_auc_score(y_test, log_reg.predict_proba(X_test)[:,1]))

# %%
# ==============================================================
# 4.2 Random Forest
# ==============================================================
rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

print("Random Forest")
print(classification_report(y_test, y_pred_rf))
print("ROC-AUC:", roc_auc_score(y_test, rf.predict_proba(X_test)[:,1]))

# %%
# ==============================================================
# 4.3 XGBoost
# ==============================================================
xgb = XGBClassifier(eval_metric="logloss", random_state=42)
xgb.fit(X_train, y_train)
y_pred_xgb = xgb.predict(X_test)

print("XGBoost")
print(classification_report(y_test, y_pred_xgb))
print("ROC-AUC:", roc_auc_score(y_test, xgb.predict_proba(X_test)[:,1]))

# %% [markdown]
# # 5. Interpretabilidad

# %%
# ==============================================================
# 5.1 Feature importance - Random Forest
# ==============================================================
importances = rf.feature_importances_
indices = np.argsort(importances)[-10:]  # Top 10

plt.figure(figsize=(8,6))
plt.barh(range(len(indices)), importances[indices], align="center", color='skyblue')
plt.yticks(range(len(indices)), [columnas[i] for i in indices])
plt.xlabel("Importancia")
plt.title("Top 10 Variables más importantes (Random Forest)")
plt.show()

# %%
# ==============================================================
# 5.2 SHAP para XGBoost
# ==============================================================
explainer = shap.TreeExplainer(xgb)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test, feature_names=columnas)

# %% [markdown]
# # 6. Columna de predicción tras entrenamiento del modelo

# %%
# Probabilidad de churn
df["Probabilidad_Baja"] = xgb.predict_proba(X_scaled)[:,1]

# Predicción final (0 = no churn, 1 = churn)
df["Prediccion_Baja"] = xgb.predict(X_scaled)

# %% [markdown]
# # 7 Revertir Columnas Binarias

# %%
cols_originales = ["Género", "Pareja", "Dependientes", "Servicio_Teléfono", "Factura_Electrónica"]

for col in cols_originales:
    df[col] = encoders[col].inverse_transform(df[col])

# %% [markdown]
# # 8 Recuperamos CustomerID

# %%
# Reinsertar customerID para el CSV final
df["customerID"] = customer_ids.values
df.rename(columns={"customerID": "ClienteID"}, inplace=True)

# %% [markdown]
# # 8 Guardar Dataset limpio

# %%
# Ruta de salida del CSV con predicciones
output_csv = project_dir / "Data" / "Predicciones_Telco.csv"

# Crear carpeta Data si no existe
output_csv.parent.mkdir(parents=True, exist_ok=True)

# Guardar CSV
df.to_csv(
    output_csv,
    index=False,
    sep=";",        # Power BI en español suele usar punto y coma
    decimal=".",    # números decimales con punto
    encoding="utf-8-sig"
)

print("CSV guardado en:", output_csv)


# %% [markdown]
# # 9 Guardar CSV con el ranking de variables más importantes

# %%
# Crear DataFrame con variables e importancia
df_importance = pd.DataFrame({
    'Variable': columnas,                 # nombres de columnas usadas en el modelo
    'Importancia': rf.feature_importances_
})

# Ordenar de mayor a menor
df_importance = df_importance.sort_values(by='Importancia', ascending=False)

# Guardar solo el top 10
top10_rf = df_importance.head(10)

# Ruta de salida
output_top10_rf = project_dir / "Data" / "Top10_Variables_RF.csv"

# Crear carpeta si no existe
output_top10_rf.parent.mkdir(parents=True, exist_ok=True)

# Guardar CSV
top10_rf.to_csv(output_top10_rf, index=False, sep=";", decimal=".", encoding="utf-8-sig")

print("CSV Top 10 RF guardado en:", output_top10_rf)



