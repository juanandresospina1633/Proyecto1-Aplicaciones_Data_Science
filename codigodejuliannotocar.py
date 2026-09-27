import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


df = pd.read_csv("Características y composición del hogar.csv", sep=";")

df_mayores18 = df[df["P6040"] >= 18]

df_bogota = df_mayores18[df_mayores18["P753S1"] == 11].copy()



# df_bogota["FEX_C"] = df_bogota["FEX_C"].astype(str).str.replace(",", ".").astype(float)
# df_bogota['FEX_C'].head(20)
# media_ponderada = np.average(df_bogota['P1896'], weights=df_bogota['FEX_C'])

# media_ponderada

# Diccionario de categorías étnicas para la creación del gráfico
etnias = {
    1: "Indígena",
    5: "Negro/Afro",
    6: "Ninguno"
}
# Reemplazar valores de "99" en la variable de satisfacción de ingresos por NaN.
df_bogota["P1896"] = df_bogota["P1896"].replace(99,np.nan)
# Crear una nueva variable con los grupos étnicos con la función .map
df_bogota["grupo_etnico"] = df["P6080"].map(etnias)


# GRÁFICO 1: SATISFACCION PROMEDIO CON EL INGRESO SEGÚN GRUPO ÉTNICO

# Se calcula el promedio de la variable de satisfaccion de ingreso por el grupo étnico
prom_ingreso = (
    df_bogota.groupby("grupo_etnico")["P1896"]
    .mean()
    # .sort_values(ascending=False)
)
#(pruebas)
# print(df_bogota['P1896'].value_counts())
# print(df_bogota['P1898'].value_counts())

plt.figure(figsize=(10,6))
sns.barplot(
    x=prom_ingreso.index,
    y=prom_ingreso.values,
    palette="Blues_d"
)

plt.title("Satisfacción promedio con el ingreso según grupo étnico")
plt.xlabel("Grupo étnico")
plt.ylabel("Promedio satisfacción (0-10)")
plt.xticks(rotation=45)
plt.ylim(0,10)
# Se añaden los valores encima de las barras como texto
for i, v in enumerate(prom_ingreso.values):
    plt.text(i, v+0.1, f"{v:.2f}", ha='center')
plt.tight_layout()
plt.show()


# GRÁFICO 2: SATISFACCION SEGURIDAD

# Se calculan los promedios por grupo étnico.
prom_seguridad = (
    df_bogota.groupby("grupo_etnico")["P1898"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,6))
sns.barplot(
    x=prom_seguridad.index,
    y=prom_seguridad.values,
    palette="Greens_d"
)

plt.title("Satisfacción promedio con la seguridad según grupo étnico")
plt.xlabel("Grupo étnico")
plt.ylabel("Promedio satisfacción (0-10)")
plt.xticks(rotation=45)
plt.ylim(0,10)
# Se añaden los valores encima de las barras como texto
for i, v in enumerate(prom_seguridad.values):
    plt.text(i, v+0.1, f"{v:.2f}", ha='center')
plt.tight_layout()
plt.show()
