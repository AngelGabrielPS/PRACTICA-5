#CASO 1

# Paso 1: Filtrar alojamientos que cumplan con los criterios
filtro = (df_airbnb["number_of_reviews"] > 10) & (df_airbnb["review_scores_rating"] > 4)

# Aplicar el filtro
alojamientos_filtrados = df_airbnb[filtro]

# Paso 2: Ordenar los alojamientos
alojamientos_ordenados = alojamientos_filtrados.sort_values(by=["review_scores_rating", "number_of_reviews"], ascending=[False, False])

# Paso 3: Seleccionar las tres mejores opciones
tres_mejores_opciones = alojamientos_ordenados.head(3)

# Mostrar las tres mejores opciones
print(tres_mejores_opciones)



#CASO 2
import pandas as pd

# Filtrar las propiedades de Roberto (ID: 97503) y Clara (ID: 90387)
roberto_id = 97503
clara_id = 90387

propiedades_roberto = df_airbnb[df_airbnb["id"] == roberto_id]
propiedades_clara = df_airbnb[df_airbnb["id"] == clara_id]

# Concatenar los DataFrames de Roberto y Clara
propiedades_roberto_clara = pd.concat([propiedades_roberto, propiedades_clara])

# Guardar el DataFrame en un archivo Excel llamado "roberto.xls"
propiedades_roberto_clara.to_excel("roberto.xls", index=False)



#CASO 3 

# Paso 1: Filtrar propiedades dentro del presupuesto de Diana (<= 50€)
presupuesto_maximo = 50
propiedades_diana = df_airbnb[df_airbnb["price"] <= presupuesto_maximo]

# Paso 2: Filtrar propiedades compartidas (room_type == Shared room)
propiedades_compartidas = propiedades_diana[propiedades_diana["room_type"] == "Shared room"]

# Paso 3: Ordenar las propiedades compartidas por puntuación y seleccionar las 10 mejores
propiedades_compartidas_ordenadas = propiedades_compartidas.sort_values(by=["review_scores_rating"], ascending=False).head(10)

# Paso 4: Si aún no tenemos 10 propiedades compartidas, completar con otras propiedades dentro del presupuesto
numero_propiedades_faltantes = 10 - len(propiedades_compartidas_ordenadas)

if numero_propiedades_faltantes > 0:
    # Filtrar propiedades privadas dentro del presupuesto
    propiedades_privadas = propiedades_diana[propiedades_diana["room_type"] == "Private room"]
    
    # Ordenar las propiedades privadas por precio y seleccionar las restantes
    propiedades_privadas_ordenadas = propiedades_privadas.sort_values(by=["price"]).head(numero_propiedades_faltantes)
    
    # Concatenar las propiedades compartidas y privadas seleccionadas
    propiedades_seleccionadas = pd.concat([propiedades_compartidas_ordenadas, propiedades_privadas_ordenadas])
else:
    propiedades_seleccionadas = propiedades_compartidas_ordenadas

# Mostrar las 10 propiedades seleccionadas
print(propiedades_seleccionadas)



#CASO 1

import matplotlib.pyplot as plt

# Contar la cantidad de cada tipo de habitación
habitaciones_por_tipo = df_airbnb["room_type"].value_counts()

# Crear una lista de colores para el gráfico
colores = ["gold", "lightskyblue", "lightcoral", "lightgreen"]

# Crear una figura y ejes para el gráfico circular
fig, ax = plt.subplots()

# Crear el gráfico circular
ax.pie(habitaciones_por_tipo, labels=habitaciones_por_tipo.index, autopct="%1.1f%%", startangle=90, colors=colores)

# Agregar un título
ax.set_title("Distribución de tipos de habitaciones")

# Mostrar el gráfico
plt.show()
