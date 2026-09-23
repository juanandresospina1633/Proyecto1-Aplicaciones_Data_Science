import pandas as pd

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

print("felicidad hombres y mujeres")
df_bogota_hombres=df_bogota[df_bogota["P6020"] ==1]
df_bogota_hombres_felices=df_bogota_hombres[df_bogota_hombres["P1895"]>=8]
df_bogota_mujeres=df_bogota[df_bogota["P6020"] ==2]
df_bogota_mujeres_felices=df_bogota_mujeres[df_bogota_mujeres["P1895"]>=8]
# 6. Guardar el dataset filtrado para análisis
df_bogota.to_csv("df_bogota_filtrado.csv")
df_bogota_hombres_tristes=df_bogota_hombres[df_bogota_hombres["P1895"]<8]
df_bogota_mujeres_tristes=df_bogota_mujeres[df_bogota_mujeres["P1895"]<8]
print(len(df_bogota_hombres))
print(len(df_bogota_mujeres))
print(len(df_bogota_hombres_felices))
print(len(df_bogota_hombres_tristes))
print(len(df_bogota_mujeres_felices))
print(len(df_bogota_mujeres_tristes))

print("campesinos felices")
df_bogota_campesinos=df_bogota[df_bogota["P2057"]==1]
df_bogota_campesinos_felices=df_bogota_campesinos[df_bogota_campesinos["P1895"]>=8]
df_bogotanos_felices=df_bogota[df_bogota["P1895"]>=8]
print(len(df_bogota_campesinos_felices)/len(df_bogota_campesinos))
print(len(df_bogotanos_felices)/len(df_bogota))

print("felicidad por edad")
df_adolescentes_tristes=df_bogota[df_bogota["P6040"]<=23]
df_adultos_tristes=df_bogota[df_bogota["P6040"]<=40]
