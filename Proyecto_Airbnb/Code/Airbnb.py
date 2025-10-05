# %% [markdown]
# # 1.Carga y exploración inicial datos

# %%
# ==============================================================
# 1.1 Importar librerías
# ==============================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")

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
    project_dir = Path(r"D:\Cursos\Data_Analytics\Portfolio\Portfolio_Github\Proyecto_Airbnb")
elif so == "Darwin":  # Mac
    project_dir = Path("/Users/danielalvarezmiguez/Desktop/Portfolio-Power-Bi/Proyecto_Airbnb")
else:
    raise Exception("Sistema operativo no soportado")

# Ruta al CSV dentro de Data
csv_path = project_dir / "Data" / "listings.csv"

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
# 2.1 Precios y detección de outliers con IQR
# ==============================================================
df['price'] = df['price'].replace('[\€,]', '', regex=True).astype(float)

# %%
# Eliminar precios no válidos (≤ 0)
df = df[df['price'] > 0]

# %%
# Boxplot antes de limpiar
plt.figure(figsize=(6,4))
sns.boxplot(x=df['price'])
plt.title("Detección visual de outliers en precios")
plt.show()

# %%
# Cálculo del IQR
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR


# %%
# Forzar límite inferior lógico (ningún precio <= 0)
lower_bound_logico = max(lower_bound, 1)  # ajusta según consideres mínimo válido

print(f"Límite inferior lógico: {lower_bound_logico:.2f} €, Límite superior: {upper_bound:.2f} €")

# %%
# Filtrar outliers
df = df[(df['price'] >= lower_bound) & (df['price'] <= upper_bound)]

# %%
# Boxplot después de limpiar
plt.figure(figsize=(6,4))
sns.boxplot(x=df['price'], color='green')
plt.title("Precios después de eliminar outliers")
plt.show()

# %%
# ==============================================================
# 2.2 Fechas
# ==============================================================
df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')
df['days_since_last_review'] = (pd.Timestamp.today() - df['last_review']).dt.days

print(df.info())

# %%
# ==============================================================
# 2.3 Valores Nulos
# ==============================================================
df['number_of_reviews'] = df['number_of_reviews'].fillna(0)
df['reviews_per_month'] = df['reviews_per_month'].fillna(0)
df['neighbourhood'] = df['neighbourhood'].fillna('Desconocido')
df['room_type'] = df['room_type'].fillna('Desconocido')
df['host_name'] = df['host_name'].fillna('Sin persona de contacto')
df['license'] = df['license'].fillna('Sin licencia indicada')
                     
# Revisión post-tratamiento
total_filas = len(df)
nulos = df.isnull().sum()
porcentaje_nulos = (nulos / total_filas) * 100

resultado_post = pd.DataFrame({
    'Nulos': nulos,
    'Porcentaje (%)': porcentaje_nulos.round(2)
}).sort_values(by='Porcentaje (%)', ascending=False)

print("Valores nulos después del tratamiento:\n", resultado_post)

# %%
# ==============================================================
# 2.4 Duplicados
# ==============================================================
df = df.drop_duplicates(subset='id')

print("Dimensiones del dataset:", df.shape)

# %%
# ==============================================================
# 2.5 Normalizar texto de variables categóricas
# ==============================================================
df['room_type'] = df['room_type'].str.strip().str.title()
if 'neighbourhood_group' in df.columns:
    df['neighbourhood_group'] = df['neighbourhood_group'].fillna('Sin dato')

# %%
df['name'] = df['name'].str.title().str.strip()

print(df['name'].head(10))

# %%
# ==============================================================
# 2.6 Renombrar columnas
# ==============================================================
df = df.rename(columns={'id': 'ID', 'name': 'Nombre_Alojamiento', 'host_id': 'ID_Anfitrión', 'host_name': 'Nombre_Anfitrión', 'neighbourhood': 'Barrio', 'neighbourhood_group': 'Zona', 'latitude': 'Latitud', 'longitude': 'Longitud', 'room_type': 'Tipo_Habitación', 'price': 'Precio', 'minimum_nights': 'Noches_Mínimas', 'number_of_reviews': 'Número_de_Reseñas', 'last_review': 'Última_Reseña', 'reviews_per_month': 'Reseñas_por_Mes', 'calculated_host_listings_count': 'Alojamientos_del_Anfitrión', 'availability_365': 'Disponibilidad_365_días', 'days_since_last_review': 'Días_desde_última_reseña', 'license': 'Licencia', 'number_of_reviews_ltm': 'Número_de_Reseñas_Últimos_12_meses'})

# %% [markdown]
# # 3 Análisis Exploratorio EDA

# %%
# ==============================================================
# 3.1 Distribución de precios
# ==============================================================
plt.figure(figsize=(8,4))
sns.histplot(df['Precio'], bins=50, kde=True, color='teal')
plt.title("Distribución de precios de Airbnb Madrid")
plt.xlabel("Precio")
plt.show()

# %%
# ==============================================================
# 3.2 Top 10 barrios con más alojamientos
# ==============================================================
top_neighbourhoods = df['Barrio'].value_counts().head(10)

plt.figure(figsize=(8,4))
sns.barplot(
    x=top_neighbourhoods.values,
    y=top_neighbourhoods.index,
    hue=top_neighbourhoods.index,
    palette="viridis",
    dodge=False,                    
    legend=False                   
)
plt.title("Top 10 barrios con más alojamientos")
plt.xlabel("Número de alojamientos")
plt.ylabel("Barrio")
plt.show()

# %%
# ==============================================================
# 3.3 Relación precio vs número de reviews
# ==============================================================
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x='Número_de_Reseñas', y='Precio', alpha=0.5)
plt.title("Precio vs Número de Reseñas")
plt.xlabel("Número de Reseñas")
plt.ylabel("Precio")
plt.show()

# %%
# ==============================================================
# 3.4 Distribución del tipo de habitación
# ==============================================================
plt.figure(figsize=(6,4))
sns.countplot(
    data=df,
    x='Tipo_Habitación',
    hue=df['Tipo_Habitación'],  
    palette="Set2",
    dodge=False,
    legend=False
)
plt.title("Distribución de tipo de habitación")
plt.show()

# %%
# ==============================================================
# 3.5  Precio promedio por tipo de habitación
# ==============================================================
avg_price_room = df.groupby('Tipo_Habitación')['Precio'].mean().sort_values()

plt.figure(figsize=(6,4))
sns.barplot(
    x=avg_price_room.values,
    y=avg_price_room.index,
    hue=avg_price_room.index, 
    palette="coolwarm",
    dodge=False,
    legend=False
)
plt.title("Precio promedio por tipo de habitación")
plt.xlabel("Precio promedio (€)")
plt.show()

# %%
# ==============================================================
# 3.6  Precio promedio por barrio (Top 10)
# ==============================================================
avg_price_neigh = df.groupby('Barrio')['Precio'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(8,4))
sns.barplot(
    x=avg_price_neigh.values,
    y=avg_price_neigh.index,
    hue=avg_price_neigh.index,
    palette="magma",
    dodge=False,
    legend=False
)
plt.title("Top 10 barrios con precio promedio más alto")
plt.xlabel("Precio promedio (€)")
plt.ylabel("Barrio")
plt.show()

# %% [markdown]
# # 3 Guardar Dataframe limpio

# %%
# Ruta de salida del CSV limpio
output_csv = project_dir / "Data" / "listings_limpio.csv"

# Guardar CSV limpio
df.to_csv(
    output_csv,
    index=False,
    sep=";",        # separador de columnas (Power BI en español lo espera)
    decimal=".",    # lat/lon se guardan con punto decimal
    encoding="utf-8-sig"
)

print("CSV guardado en:", output_csv)


