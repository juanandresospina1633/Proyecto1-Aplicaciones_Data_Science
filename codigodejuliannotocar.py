import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


df = pd.read_csv("Características y composición del hogar.csv", sep=";")
df_mayores18 = df[df["P6040"] >= 18]
df_bogota = df_mayores18[df_mayores18["P753S1"] == 11].copy()

# LIMPIEZA
# Se cambian los valores de la variable factor de expansión por numéricos (float)
df_bogota["FEX_C"] = pd.to_numeric(
    df_bogota["FEX_C"].str.replace(",", ".", regex=False),
    errors="coerce"
)
# Se limpia la variable P1896 de valores inválidos
df_bogota["P1896"] = df_bogota["P1896"].replace(99,np.nan)


# Diccionario de categorías étnicas para los gráficos
etnias = {
    1: "Indígena",
    5: "Negro/Afro",
    6: "Ninguno"
}
df_bogota["grupo_etnico"] = df_bogota["P6080"].map(etnias)


# SATISFACCIÓN CON INGRESO

df_ingreso = df_bogota.dropna(subset=["P1896", "FEX_C", "grupo_etnico"])

prom_ingreso = (
    df_ingreso.groupby("grupo_etnico").apply(lambda x: (x["P1896"] * x["FEX_C"]).sum() / x["FEX_C"].sum())
)


plt.figure(figsize=(10,6))
sns.barplot(
    x=prom_ingreso.index,
    y=prom_ingreso.values,
    palette="Blues_d"
)

plt.title("Satisfacción promedio con el ingreso según grupo étnico (ponderada)")
plt.xlabel("Grupo étnico")
plt.ylabel("Promedio satisfacción (0-10)")
plt.xticks(rotation=45)
plt.ylim(0,10)
for i, v in enumerate(prom_ingreso.values):
    plt.text(i, v+0.1, f"{v:.2f}", ha='center')
plt.tight_layout()
plt.show()


# SATISFACCION SEGURIDAD
df_seguridad = df_bogota.dropna(subset=["P1898", "FEX_C", "grupo_etnico"])
prom_seguridad = (
    df_seguridad.groupby("grupo_etnico").apply(lambda x: (x["P1898"] * x["FEX_C"]).sum() / x["FEX_C"].sum())
)

plt.figure(figsize=(10,6))
sns.barplot(
    x=prom_seguridad.index,
    y=prom_seguridad.values,
    palette="Greens_d"
)

plt.title("Satisfacción promedio con la seguridad según grupo étnico (ponderada)")
plt.xlabel("Grupo étnico")
plt.ylabel("Promedio satisfacción (0-10)")
plt.xticks(rotation=45)
plt.ylim(0,11)
for i, v in enumerate(prom_seguridad.values):
    plt.text(i, v+0.1, f"{v:.2f}", ha='center')
plt.tight_layout()
plt.show()
