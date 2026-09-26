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

# Si el separador decimal es coma, reemplázala por punto antes de convertir
df_bogota["FEX_C"] = df_bogota["FEX_C"].astype(str).str.replace(",", ".").astype(float)

print("bienestar por etnia")

df_bogota_indigenas = df_bogota.loc[df_bogota["P6080"] == 1, ["P1895","P1896","P1897","P1898","P1899","P3175","P1901","P1903","P1904","P1905","P1927","FEX_C"]]
df_bogota_negros = df_bogota.loc[df_bogota["P6080"] == 5, ["P1895","P1896","P1897","P1898","P1899","P3175","P1901","P1903","P1904","P1905","P1927","FEX_C"]]
df_bogota_sin_etnia = df_bogota.loc[df_bogota["P6080"] == 6, ["P1895","P1896","P1897","P1898","P1899","P3175","P1901","P1903","P1904","P1905","P1927","FEX_C"]]

n_indigenas_bogota = len(df_bogota_indigenas)
n_afro_bogota = len(df_bogota_negros)

print(f"Personas indígenas en la muestra de Bogotá: {n_indigenas_bogota}")
print(f"Personas afro en la muestra de Bogotá: {n_afro_bogota}")

sns.set(style="whitegrid")

# Diccionario de grupos y colores
grupos = {
    "Indígena": (df_bogota_indigenas, "red"),
    "Afro": (df_bogota_negros, "blue")
}
## Reconocer que cantidad de población representan los individuos encuestados
poblacion_indigena = df_bogota_indigenas["FEX_C"].sum()
poblacion_afro = df_bogota_negros["FEX_C"].sum()

print(f"Población indígena estimada en Bogotá segun el Factor de expansión: {poblacion_indigena:,.0f}")
print(f"Población afro estimada en Bogotá según el Factor de expansión: {poblacion_afro:,.0f}")

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
df_combinado = pd.concat(
    [df.assign(grupo_etnico=nombre) for nombre, (df, color) in grupos.items()],
    ignore_index=True
)

sns.boxplot(data=df_combinado, x='grupo_etnico', y='P1904',
            palette={'Indígena': 'red', 'Afro': 'blue'})
plt.ylabel("P1904 (0 = Para nada triste, 10 = Todo el tiempo triste)")
plt.xlabel("Grupo étnico")
plt.title("Distribución de tristeza por grupo étnico")
plt.show()

## Grafico de observación 10 ----- P1905: ¿Qué tanto considera...que las cosas que hace en su vida valen la pena?
sns.boxplot(data=df_combinado, x='grupo_etnico', y='P1905',
            palette={'Indígena': 'red', 'Afro': 'blue'})
plt.ylabel("P1905 (0 = No valen la pena, 10 = Valen totalmente la pena)")
plt.xlabel("Grupo étnico")
plt.title("Distribución de '¿qué tanto vale la pena su vida?' por grupo étnico")
plt.show()

## Grafico de observación 11 ---- P1927: ¿En cuál escalón diría usted que se encuentra parado/a en este momento?
sns.boxplot(data=df_combinado, x='grupo_etnico', y='P1927',
            palette={'Indígena': 'red', 'Afro': 'blue'})
plt.ylabel("P1927 (0 = Peor vida, 10 = Mejor vida)")
plt.xlabel("Grupo étnico")
plt.title("Distribución de '¿en qué escalón se encuentra?' por grupo étnico")
plt.show()