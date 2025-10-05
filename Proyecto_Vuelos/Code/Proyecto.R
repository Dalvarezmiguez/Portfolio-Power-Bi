#-----------------------------------------------
# 1. Carga archivos
#-----------------------------------------------

# 1.1 Instalar paquetes
install.packages(c("data.table", "tidyverse"))

# 1.2 Activar librería
library(tidyverse)
library(data.table)
library(dplyr)

# 1.3 Cargar dataset
df <- fread("../Data/flight_data_2024.csv")

# 1.4 Ver dataset
View(df)

# 1.5 Ver tipos de columnas
str(df)

#-----------------------------------------------
# 2. Limpieza
#-----------------------------------------------

# 2.1 Elegir columnas 
df_limpio <- df %>%
  select(
    fl_date,
    op_unique_carrier, 
    op_carrier_fl_num,
    origin_state_nm,
    dest_state_nm,
    dep_delay,
    arr_delay,
    taxi_out,
    taxi_in,
    air_time,
    distance,
    cancelled,
    cancellation_code,
    carrier_delay,
    weather_delay,
    nas_delay,
    security_delay,
    late_aircraft_delay
  )

# 2.2 Cambiar nombres columnas
df_limpio <- df_limpio %>%
  rename(
    Fecha = fl_date,
    Aerolinea = op_unique_carrier, 
    Numero_Vuelo = op_carrier_fl_num,
    Origen = origin_state_nm,
    Destino = dest_state_nm,
    Retraso_Salida = dep_delay,
    Retraso_Llegada = arr_delay,
    Tiempo_Pista_Salida = taxi_out,
    Tiempo_Pista_Llegada = taxi_in,
    Tiempo_Vuelo = air_time,
    Distancia = distance,
    Cancelado = cancelled,
    CancelacionID = cancellation_code,
    Retraso_Compañia = carrier_delay,
    Retraso_Tiempo = weather_delay,
    Retraso_Nacional = nas_delay,
    Retraso_Seguridad = security_delay,
    Retraso_Avion = late_aircraft_delay
  )

# 2.3 Revisar duplicados exactos
sum(duplicated(df_limpio))

#Eliminar duplicados si los hay
df_limpio <- df_limpio %>% distinct()

# 2.4 Número de NA por columna
colSums(is.na(df_limpio))

# Reemplazar NAs en retrasos por 0
df_limpio <- df_limpio %>%
  mutate(across(c(Retraso_Salida, 
                  Retraso_Llegada, 
                  Tiempo_Pista_Salida, 
                  Tiempo_Pista_Llegada,
                  Tiempo_Vuelo,
                  Retraso_Compañia,
                  Retraso_Tiempo,
                  Retraso_Nacional,
                  Retraso_Seguridad, 
                  Retraso_Avion), ~replace_na(., 0)))

# Revisar de nuevo
colSums(is.na(df_limpio))

# Eliminar columna Numero_Vuelo NA
df_limpio <- df_limpio %>%
  filter(!is.na(Numero_Vuelo))

# 2.5 Limpiar espacios en texto
df_limpio <- df_limpio %>%
  mutate(
    Aerolinea = trimws(Aerolinea),
    Origen = trimws(Origen),
    Destino = trimws(Destino),
    CancelacionID = trimws(CancelacionID)
  )

# 2.6 Ver tipos de columnas
str(df_limpio)

# Convertir tipos
df_limpio <- df_limpio %>%
  mutate(
    Fecha = as.Date(Fecha),
    Retraso_Salida = as.integer(Retraso_Salida),
    Retraso_Llegada = as.integer(Retraso_Llegada),
    Tiempo_Pista_Salida = as.integer(Tiempo_Pista_Salida),
    Tiempo_Pista_Llegada = as.integer(Tiempo_Pista_Llegada),
    Tiempo_Vuelo = as.integer(Tiempo_Vuelo),
    Distancia = as.integer(Distancia)
  )

# 2.6 Ver resumen dataset limpio
summary(df_limpio)

#-----------------------------------------------
# 3. Guardar Dataset
#-----------------------------------------------
fwrite(df_limpio, "../Data/flight_data_limpio.csv")

