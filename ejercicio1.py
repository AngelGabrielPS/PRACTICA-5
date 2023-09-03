#importa pandas
import pandas as pd


#Crear una Serie
serie = pd.Series([10, 20, 10])
print(serie)


# Crear un DataFrame vacío llamado 'df'
df = pd.DataFrame()
print(df)


# Crea una nueva columna en el dataframe, y asignale la primera serie que has creado
serie = pd.Series([10, 20, 10])
df = pd.DataFrame()
df["nueva_columna"] = serie
print(df)



# Crea otra columna en el dataframe y asignale la segunda Serie que has creado
serie1 = pd.Series([10, 20, 10])
serie2 = pd.Series([30, 40, 50])
df = pd.DataFrame()
df["columna1"] = serie1
df["columna2"] = serie2
print(df)


# Lee el archivo llamado 'avengers.csv" localizado en la carpeta "data" y crea un DataFrame, llamado 'avengers'. 
archivo_csv = "data/avengers.csv"
avengers = pd.read_csv(archivo_csv)


# Muestra las primeras 5 filas del DataFrame.
primeras_5_filas = avengers.head()
print(primeras_5_filas)


# Muestra las primeras 10 filas del DataFrame. 
primeras_10_filas = avengers.head(10)
print(primeras_10_filas)

# Muestra las últimas 5 filas del DataFrame.
ultimas_5_filas = avengers.tail()
print(ultimas_5_filas)

# Muestra el tamaño del DataFrame
tamaño = avengers.shape
print("El tamaño del DataFrame es:", tamaño)

# Muestra los data types del dataframe
tipos_de_datos = avengers.dtypes
print(tipos_de_datos)

# Cambia el indice a la columna "fecha_inicio".
avengers = avengers.set_index("fecha_inicio")
print(avengers)

# Ordena el índice de forma descendiente
avengers = avengers.sort_index(ascending=False)
print(avengers)

# Resetea el índice
avengers = avengers.reset_index(drop=True)
print(avengers)

