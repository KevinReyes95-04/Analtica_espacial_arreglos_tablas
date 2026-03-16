# ----------------------------------------------
# Taller: Vectorización y Álgebra Espacial con Pandas
# ----------------------------------------------

# 1. Creamos un dataframe  para estaciones meteorológicas con datos faltantes
import pandas as pd

estaciones_meteorologicas = {
    "Estación": ["Páramo", "Valle", "Costa", "Selava", "Sabada"],
    "elevación": [3200, 1500, 15, 200, 2600],
    "Precipitación": [850.5, 1200.0, None, 3000.5, None]
}
df_estaciones = pd.DataFrame(estaciones_meteorologicas)
print("Datos originales con valores faltantes:")
print(df_estaciones)

# 2. Limpieza de datos: Rellenar valores faltantes con la media de precipitación
media_precipitacion = df_estaciones["Precipitación"].mean()
df_limpio = df_estaciones.fillna(value={"Precipitación": media_precipitacion})
print(f"\nDatos después de la limpieza (valores faltantes rellenados con la media = {media_precipitacion:.1f}):")
print(df_limpio)

# 3. Filtrado: Extraer estaciones con elevación mayor a 1000 metros
df_filtrado = df_limpio[df_limpio["elevación"] > 1000]
print(f"\nEstaciones con elevación mayor a 1000 metros:")
print(df_filtrado)

# 4. Calculo final precipitacion promedio  de las estaciones altas
media_filtrada = df_filtrado["Precipitación"].mean()
print(f"\nPrecipitación promedio de las estaciones filtradas: {media_filtrada:.1f} mm")
