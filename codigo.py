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

# 5. Convertimos la variable FEX_C de tipo string a float
# Se reemplaza la coma por punto y luego se convierte a float
df_bogota['FEX_C'] = df_bogota['FEX_C'].astype(str).str.replace(',', '.', regex=False).astype(float)

# 6. Mostrar cuántos registros había antes y después del filtro
print("Total registros originales:", len(df))
print("Registros mayores de 18:", len(df_mayores18))
print("Registros mayores de 18 que vivieron en Bogotá:", len(df_bogota))

# Si el separador decimal es coma, reemplázala por punto antes de convertir
df_bogota["FEX_C"] = df_bogota["FEX_C"].astype(str).str.replace(",", ".").astype(float)

print("bienestar por etnia")

df_bogota_indigenas = df_bogota.loc[df_bogota["P6080"] == 1, ["FEX_C","P1895","P1896","P1897","P1898","P1899","P3175","P1901","P1903","P1904","P1905","P1927"]]
df_bogota_negros = df_bogota.loc[df_bogota["P6080"] == 5, ["FEX_C","P1895","P1896","P1897","P1898","P1899","P3175","P1901","P1903","P1904","P1905","P1927"]]
df_bogota_sin_etnia = df_bogota.loc[df_bogota["P6080"] == 6, ["FEX_C","P1895","P1896","P1897","P1898","P1899","P3175","P1901","P1903","P1904","P1905","P1927"]]


n_indigenas_bogota = len(df_bogota_indigenas)
n_afro_bogota = len(df_bogota_negros)

print(f"Personas indígenas en la muestra de Bogotá: {n_indigenas_bogota}")
print(f"Personas afro en la muestra de Bogotá: {n_afro_bogota}")

## Reconocer que cantidad de población representan los individuos encuestados
poblacion_indigena = df_bogota_indigenas["FEX_C"].sum()
poblacion_afro = df_bogota_negros["FEX_C"].sum()

print(f"Población indígena estimada en Bogotá segun el Factor de expansión: {poblacion_indigena:,.0f}")
print(f"Población afro estimada en Bogotá según el Factor de expansión: {poblacion_afro:,.0f}")

## reconocer el factor de expansión de cada persona
print("Factor de expansión - Indígenas")
print(df_bogota_indigenas[["FEX_C"]].to_string(index=False))

print("\nFactor de expansión - Afro")
print(df_bogota_negros[["FEX_C"]].to_string(index=False))

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


df_combinado = pd.concat(
    [df.assign(grupo_etnico=nombre) for nombre, (df, color) in grupos.items()],
    ignore_index=True
)
##Grafico de observación 9 -----  P1904: ¿Que tan triste se sintio el dia de ayer?
sns.boxplot(data=df_combinado, x='grupo_etnico', y='P1904',
            palette={'Indígena': 'red', 'Afro': 'blue'})
plt.ylabel("P1904 (0 = Para nada triste, 10 = Todo el tiempo triste)")
plt.xlabel("Grupo étnico")
plt.title("Distribución de tristeza por grupo étnico")
plt.show()

plt.figure(figsize=(8,6))

for nombre_grupo, (df, color) in grupos.items():
    plt.scatter(
        [nombre_grupo] * len(df),      # eje X: nombre del grupo (categórico)
        df["P1904"],                   # eje Y: valor de tristeza
        s=df["FEX_C"] * 3,             # tamaño del punto proporcional al peso poblacional
        color=color,
        alpha=0.6,
        edgecolor="black",
        label=nombre_grupo
    )

plt.ylabel("P1904 (0 = Para nada triste, 10 = Todo el tiempo triste)")
plt.xlabel("Grupo étnico")
plt.title("Tristeza por grupo étnico (tamaño del punto = factor de expansión FEX_C)")
plt.show()

## Grafico de observación 10 ----- P1905: ¿Qué tanto considera...que las cosas que hace en su vida valen la pena?

sns.boxplot(data=df_combinado, x='grupo_etnico', y='P1905',
            palette={'Indígena': 'red', 'Afro': 'blue'})
plt.ylabel("P1905 (0 = No valen la pena, 10 = Valen totalmente la pena)")
plt.xlabel("Grupo étnico")
plt.title("Distribución de '¿qué tanto vale la pena su vida?' por grupo étnico")
plt.show()

plt.figure(figsize=(8,6))

for nombre_grupo, (df, color) in grupos.items():
    plt.scatter(
        [nombre_grupo] * len(df),
        df["P1905"],
        s=df["FEX_C"] * 3,
        color=color,
        alpha=0.6,
        edgecolor="black",
        label=nombre_grupo
    )

plt.ylabel("P1905 (0 = No valen la pena, 10 = Valen totalmente la pena)")
plt.xlabel("Grupo étnico")
plt.title("¿Vale la pena su vida? por grupo étnico (tamaño del punto = FEX_C)")
plt.show()

## Grafico de observación 11 ---- P1927: ¿En cuál escalón diría usted que se encuentra parado/a en este momento?

sns.boxplot(data=df_combinado, x='grupo_etnico', y='P1927',
            palette={'Indígena': 'red', 'Afro': 'blue'})
plt.ylabel("P1927 (0 = Peor vida, 10 = Mejor vida)")
plt.xlabel("Grupo étnico")
plt.title("Distribución de '¿en qué escalón se encuentra?' por grupo étnico")
plt.show()

plt.figure(figsize=(8,6))

for nombre_grupo, (df, color) in grupos.items():
    plt.scatter(
        [nombre_grupo] * len(df),
        df["P1927"],
        s=df["FEX_C"] * 3,
        color=color,
        alpha=0.6,
        edgecolor="black",
        label=nombre_grupo
    )

plt.ylabel("P1927 (0 = Peor vida, 10 = Mejor vida)")
plt.xlabel("Grupo étnico")
plt.title("Escalón de vida por grupo étnico (tamaño del punto = FEX_C)")
plt.show()

# Función auxiliar sumar el factor de expansión
def preparar_datos(df_subset, variable_analizada):
  df_subset = df_subset.copy()

  resultado = df_subset.groupby(variable_analizada)['FEX_C'].sum()
  niveles_completos = range(11)
  resultado = resultado.reindex(niveles_completos, fill_value=0)
  return resultado

## Grafico de observación 12 ---- P3175: En general, ¿qué tan satisfecho/a se siente _____ con su tiempo libre?

# Se separan las columnas que se van a utilizar para cada etnia
indigenas_tiempolibre = df_bogota_indigenas[['P3175', 'FEX_C']]
negros_tiempolibre = df_bogota_negros[['P3175', 'FEX_C']]
sin_etnia_tiempolibre = df_bogota_sin_etnia[['P3175', 'FEX_C']]

# Se obtienen las frecuencias para cada grupo teniendo en cuenta el factor de expansión
datos_indigenas_tiempolibre = preparar_datos(indigenas_tiempolibre, 'P3175')
datos_negros_tiempolibre = preparar_datos(negros_tiempolibre, 'P3175')
datos_sin_etnia_tiempolibre = preparar_datos(sin_etnia_tiempolibre, 'P3175')

# Se crea una figura con 3 gráficos de barras con EJES Y INDEPENDIENTES (sharey=False)
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 5), sharey=False)

# Se asigna el título
fig.suptitle(
    'Frecuencia de Satisfación con el tiempo libre (P3175) por Grupo Étnico\n(Población expandida'
    ' con FEX_C - Escalas independientes)',
    fontsize=15,
    weight='bold',
    y=1.02,
)

# Datos, títulos y colores para cada gráfico
grupos = [
    (datos_indigenas_tiempolibre, '1. Indígena', '#2b5c8f'),
    (datos_negros_tiempolibre, '5. Negro/a, mulato/a, afrodescendiente, afrocolombiano/a', '#d95f02'),
    (datos_sin_etnia_tiempolibre, '6. Ningún grupo étnico', '#7570b3'),
]

for i, (serie_datos, titulo, color) in enumerate(grupos):
  ax = axes[i]

  # Graficar barras
  serie_datos.plot(
      kind='bar', ax=ax, color=color, width=0.75, edgecolor='black'
  )

  # Personalización de cada gráfico
  ax.set_title(titulo, fontsize=12, weight='bold')
  ax.set_xlabel(
      'Satisfación con el tiempo libre (P1901)\n(0 = Totalmente insatisfecho/a, 10 = Totalmente satisfecho/a)',
      fontsize=10,
  )

  # Como cada gráfico tiene su propia escala, se muestra el eje Y en cada uno
  ax.set_ylabel(
      'Población Representada (Frecuencia ponderada FEX_C)', fontsize=10
  )

  ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
  ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
#El siguiente código se usó para guardar la figura
#plt.savefig('Satisfación con el tiempo libre.png', bbox_inches='tight')
plt.show()

## Grafico de observación 13 ---- P1901: ¿Qué tan feliz se sintió ... el día de ayer?

# Se separan las columnas que se van a utilizar para cada etnia
indigenas_feliz = df_bogota_indigenas[['P1901', 'FEX_C']]
negros_feliz = df_bogota_negros[['P1901', 'FEX_C']]
sin_etnia_feliz = df_bogota_sin_etnia[['P1901', 'FEX_C']]

# Se obtienen las frecuencias para cada grupo teniendo en cuenta el factor de expansión
datos_indigenas_feliz = preparar_datos(indigenas_feliz, 'P1901')
datos_negros_feliz = preparar_datos(negros_feliz, 'P1901')
datos_sin_etnia_feliz = preparar_datos(sin_etnia_feliz, 'P1901')

# Se crea una figura con 3 gráficos de barras con EJES Y INDEPENDIENTES (sharey=False)
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 5), sharey=False)

# Se asigna el título
fig.suptitle(
    'Frecuencia de Felicidad (P1901) por Grupo Étnico\n(Población expandida'
    ' con FEX_C - Escalas independientes)',
    fontsize=15,
    weight='bold',
    y=1.02,
)

# Datos, títulos y colores para cada gráfico
grupos = [
    (datos_indigenas_feliz, '1. Indígena', '#2b5c8f'),
    (datos_negros_feliz, '5. Negro/a, mulato/a, afrodescendiente, afrocolombiano/a', '#d95f02'),
    (datos_sin_etnia_feliz, '6. Ningún grupo étnico', '#7570b3'),
]

for i, (serie_datos, titulo, color) in enumerate(grupos):
  ax = axes[i]

  # Graficar barras
  serie_datos.plot(
      kind='bar', ax=ax, color=color, width=0.75, edgecolor='black'
  )

  # Personalización de cada gráfico
  ax.set_title(titulo, fontsize=12, weight='bold')
  ax.set_xlabel(
      'Nivel de Felicidad (P1901)\n(0 = Para nada, 10 = Todo el tiempo)',
      fontsize=10,
  )

  # Como cada gráfico tiene su propia escala, se muestra el eje Y en cada uno
  ax.set_ylabel(
      'Población Representada (Frecuencia ponderada FEX_C)', fontsize=10
  )

  ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
  ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
#El siguiente código se usó para guardar la figura
#plt.savefig('Nivel de Felicidad.png', bbox_inches='tight')
plt.show()

## Grafico de observación 14 ---- P1903: ¿Qué tan preocupado/a se sintió ... el día de ayer?

# Se separan las columnas que se van a utilizar para cada etnia
indigenas_preocupacion = df_bogota_indigenas[['P1903', 'FEX_C']]
negros_preocupacion = df_bogota_negros[['P1903', 'FEX_C']]
sin_etnia_preocupacion = df_bogota_sin_etnia[['P1903', 'FEX_C']]

# Se obtienen las frecuencias para cada grupo teniendo en cuenta el factor de expansión
datos_indigenas_preocupacion = preparar_datos(indigenas_preocupacion, 'P1903')
datos_negros_preocupacion = preparar_datos(negros_preocupacion, 'P1903')
datos_sin_etnia_preocupacion = preparar_datos(sin_etnia_preocupacion, 'P1903')

# Se crea una figura con 3 gráficos de barras con EJES Y INDEPENDIENTES (sharey=False)
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 5), sharey=False)

# Se asigna el título
fig.suptitle(
    'Frecuencia de Preocupación del día anterior (P1903) por Grupo Étnico\n(Población expandida'
    ' con FEX_C - Escalas independientes)',
    fontsize=15,
    weight='bold',
    y=1.02,
)

# Datos, títulos y colores para cada gráfico
grupos = [
    (datos_indigenas_preocupacion, '1. Indígena', '#2b5c8f'),
    (datos_negros_preocupacion, '5. Negro/a, mulato/a, afrodescendiente, afrocolombiano/a', '#d95f02'),
    (datos_sin_etnia_preocupacion, '6. Ningún grupo étnico', '#7570b3'),
]

for i, (serie_datos, titulo, color) in enumerate(grupos):
  ax = axes[i]

  # Graficar barras
  serie_datos.plot(
      kind='bar', ax=ax, color=color, width=0.75, edgecolor='black'
  )

  # Personalización de cada gráfico
  ax.set_title(titulo, fontsize=12, weight='bold')
  ax.set_xlabel(
      'Preocupación del día anterior (P1903)\n(0 = Para nada preocupado/a, 10 = Todo el tiempo preocupado/a)',
      fontsize=10,
  )

  # Como cada gráfico tiene su propia escala, se muestra el eje Y en cada uno
  ax.set_ylabel(
      'Población Representada (Frecuencia ponderada FEX_C)', fontsize=10
  )

  ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
  ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
#El siguiente código se usó para guardar la figura
#plt.savefig('Preocupación del día anterior.png', bbox_inches='tight')
plt.show()