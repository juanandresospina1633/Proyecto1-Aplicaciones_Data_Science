import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargar los datos
df = pd.read_csv("Características y composición del hogar.csv", sep=";")

# 2. Revisar las primeras filas
print(df.head())

# 3. Filtrar por personas de 18 años o más, la variable p6040 se refiere a los años cumplidos de cada individuo
df_mayores18 = df[df["P6040"] >= 18]

# 4. Filtrar por personas que vivieron en Bogotá en los últimos 12 meses
# La variable P753S1 indica en que departamento vivio en los ultimos 12 meses, el codigo 11 del "divipola" indica a bogota
df_bogota = df_mayores18[df_mayores18["P753S1"] == 11]

# 5. Mostrar cuántos registros había antes y después del filtro
print("Total registros originales:", len(df))
print("Registros mayores de 18:", len(df_mayores18))
print("Registros mayores de 18 que vivieron en Bogotá:", len(df_bogota))

print("bienestar por etnia")

df_bogota_indigenas = df_bogota.loc[df_bogota["P6080"] == 1, ["P1895","P1896","P1897","P1898","P1899","P3175","P1901","P1903","P1904","P1905","P1927"]]
df_bogota_negros = df_bogota.loc[df_bogota["P6080"] == 5, ["P1895","P1896","P1897","P1898","P1899","P3175","P1901","P1903","P1904","P1905","P1927"]]
df_bogota_sin_etnia = df_bogota.loc[df_bogota["P6080"] == 6, ["P1895","P1896","P1897","P1898","P1899","P3175","P1901","P1903","P1904","P1905","P1927"]]


sns.set(style="whitegrid")

# Diccionario de grupos y colores
grupos = {
    "Indígena": (df_bogota_indigenas, "red"),
    "Afro": (df_bogota_negros, "blue")
}
###GRAFICOS DE DISPERSION 
# --- Gráfico 1: P1895, satisfaccion con la vida ---
plt.figure(figsize=(8,6))
for nombre, (df, color) in grupos.items():
    sns.scatterplot(x=range(len(df)), y=df["P1895"], color=color, label=nombre)
plt.title("Mapa de dispersión - satisfaccion con la vida 0-10")
plt.xlabel("Índice")
plt.ylabel("P1895")
plt.legend()
plt.show()

# --- Gráfico 2: P1897 satisfaccion con la salud---
plt.figure(figsize=(8,6))
for nombre, (df, color) in grupos.items():
    sns.scatterplot(x=range(len(df)), y=df["P1897"], color=color, label=nombre)
plt.title("Mapa de dispersión - satisfaccion con la salud 0-10")
plt.xlabel("Índice")
plt.ylabel("P1897")
plt.legend()
plt.show()

# --- Gráfico 3: P1899 satisfaccion con el trabajo o actividad---
plt.figure(figsize=(8,6))
for nombre, (df, color) in grupos.items():
    sns.scatterplot(x=range(len(df)), y=df["P1899"], color=color, label=nombre)
plt.title("Mapa de dispersión - satisfaccion con el trabajo o actividad 0-10")
plt.xlabel("Índice")
plt.ylabel("P1899")
plt.legend()
plt.show()

##Grafico de observación 9 -----  P1904: ¿Que tan triste se sintio el dia de ayer?
plt.figure(figsize=(8,6))
for var, (df,color) in grupos.items():
    sns.scatterplot(x=range(len(df)), y=df["P1904"], color=color, label=var)

plt.title("Mapa de dispersión:¿Qué tan preocupado/a se sintió ... el día de ayer?")    
plt.xlabel("Número de observación")
# Etiqueta del eje Y, indicando el significado de la escala 0-10
plt.ylabel("P1904 (0 = Para nada triste, 10 = Todo el tiempo triste)")
# Nota aclaratoria adicional debajo del gráfico sobre la escala
plt.figtext(0.5, -0.03, "Escala: 0 = Para nada triste | 10 = Todo el tiempo triste",ha="center", fontsize=9, style="italic")
plt.legend()
plt.show()

## Grafico de observación 10 ----- P1905: ¿Qué tanto considera...que las cosas que hace en su vida valen la pena?
plt.figure(figsize=(8,6))
for var, (df,color) in grupos.items():
    sns.scatterplot(x=range(len(df)), y=df["P1904"], color=color, label=var)

plt.title("Mapa de dispersión:¿Qué tanto considera...que las cosas que hace en su vida valen la pena?")    
plt.xlabel("Número de observación")
# Etiqueta del eje Y, indicando el significado de la escala 0-10
plt.ylabel("P1904 (0 = No valen la pena, 10 =  Valen totalmente la pena")
# Nota aclaratoria adicional debajo del gráfico sobre la escala
plt.figtext(0.5, -0.03, "Escala: 0 = No valen la pena | 10 =  Valen totalmente la pena",ha="center", fontsize=9, style="italic")
plt.legend()
plt.show()

## Grafico de observación 11 ---- P1927: ¿En cuál escalón diría usted que se encuentra parado/a en este momento?
plt.figure(figsize=(8,6))
for var, (df,color) in grupos.items():
    sns.scatterplot(x=range(len(df)), y=df["P1904"], color=color, label=var)

plt.title("Mapa de dispersión:¿En cuál escalón diría usted que se encuentra parado/a en este momento?")    
plt.xlabel("Número de observación")
# Etiqueta del eje Y, indicando el significado de la escala 0-10
plt.ylabel("P1904 (0 = Peor vida, 10 =   Mejor vida")
# Nota aclaratoria adicional debajo del gráfico sobre la escala
plt.figtext(0.5, -0.03, "Escala: 0 = Peor vida | 10 =  Mejor vida",ha="center", fontsize=9, style="italic")
plt.legend()
plt.show()