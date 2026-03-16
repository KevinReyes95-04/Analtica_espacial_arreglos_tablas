# ----------------------------------------------
# Taller: Vectorización y Álgebra Espacial con Pandas
# ----------------------------------------------

# 1. Importamos las librerías necesarias
import pandas as pd
import numpy as np

# 2. Construimos los datos del censo
datos_censo = {
    "Ciudad": ["Bogotá", "Medellín", "Cali", "Barranquilla"],
    "Region": ["Andina", "Andina", "Pacífica", "Caribe"],
    "Poblacion": [7181469, 2529403, 2227642, 1206319],
    "Elevacion": [2640, 1495, 1018, 18],
    "Latitud": [4.7110, 6.2442, 3.4516, 10.9685],
    "Longitud": [-74.0721, -75.5812, -76.5320, -74.7813]
}

# 3. Convertimos el diccionario en un DataFrame
df = pd.DataFrame(datos_censo)

print("DataFrame original:")
print(df)


# 4. Función vectorizada para calcular distancias desde Bogotá
def calcular_distancias(df):
    """
    Calcula de forma vectorizada la distancia en kilómetros
    desde Bogotá hacia todas las ciudades del DataFrame,
    usando la fórmula de Haversine.

    Parámetros
    ----------
    df : pandas.DataFrame
        Debe contener las columnas 'Latitud' y 'Longitud'.

    Retorna
    -------
    pandas.DataFrame
        El mismo DataFrame con una nueva columna llamada
        'Distancia_Bogota'.
    """

    # Coordenadas fijas de Bogotá
    lat_bogota = 4.7110
    lon_bogota = -74.0721

    # Convertimos todas las coordenadas a radianes
    lat1 = np.radians(lat_bogota)
    lon1 = np.radians(lon_bogota)
    lat2 = np.radians(df["Latitud"])
    lon2 = np.radians(df["Longitud"])

    # Fórmula de Haversine aplicada de forma vectorizada
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))

    # Radio de la Tierra en kilómetros
    radio_tierra = 6371

    # Agregamos la nueva columna al DataFrame
    df["Distancia_Bogota"] = np.round(radio_tierra * c, 2)

    return df


# 5. Aplicamos la función
df = calcular_distancias(df)

print("\nDataFrame con la distancia desde Bogotá:")
print(df)

