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

print("Total hombres")
print(len(df_bogota_hombres))
print("Total mujeres")
print(len(df_bogota_mujeres))
print("Hombres felices")
print(len(df_bogota_hombres_felices))

print("Mujeres felices")
print(len(df_bogota_mujeres_felices))

print("Promedio de felicidad en hombres")
print(len(df_bogota_hombres_felices)/len(df_bogota_hombres))
print("Promedio de felicidad en mujeres")
print(len(df_bogota_mujeres_felices)/len(df_bogota_mujeres))

print("campesinos felices")
df_bogota_campesinos=df_bogota[df_bogota["P2057"]==1]
df_bogota_campesinos_felices=df_bogota_campesinos[df_bogota_campesinos["P1895"]>=8]
df_bogotanos_felices=df_bogota[df_bogota["P1895"]>=8]
print("Campesinos")
print("Total campesinos")
print(len(df_bogota_campesinos))
print("Promedio campesinos felices")
print(len(df_bogota_campesinos_felices)/len(df_bogota_campesinos))
print("Bogotanos")
print("Total bogotanos")
print(len(df_bogota))
print("Promedio bogotanos felices")
print(len(df_bogotanos_felices)/len(df_bogota))

print("felicidad por edad")
df_adolescentes=df_bogota[df_bogota["P6040"]<=23]
df_jovenes_adultos=df_bogota[(df_bogota["P6040"]>23) & (df_bogota["P6040"]<=40)]
df_adultos=df_bogota[(df_bogota["P6040"]>40) & (df_bogota["P6040"]<=65)]
df_tercera_edad=df_bogota[df_bogota["P6040"]>65]

df_adolescentes_felices=df_adolescentes[df_adolescentes["P1895"]>=8]
df_jovenes_adultos_felices=df_jovenes_adultos[df_jovenes_adultos["P1895"]>=8]
df_adultos_felices=df_adultos[df_adultos["P1895"]>=8]
df_tercera_edad_felices=df_tercera_edad[df_tercera_edad["P1895"]>=8]

print("Adolescentes (18-23 años)")
print("Total adolescentes")
print(len(df_adolescentes))
print("Promedio adolescentes felices")
print(len(df_adolescentes_felices)/len(df_adolescentes))
print("Jovenes adultos (24-40 años)")
print("Total jovenes adultos")
print(len(df_jovenes_adultos))
print("Promedio jovenes adultos felices")
print(len(df_jovenes_adultos_felices)/len(df_jovenes_adultos))
print("Adultos (41-65 años)")
print("Total adultos")
print(len(df_adultos))
print("Promedio adultos felices")
print(len(df_adultos_felices)/len(df_adultos))
print("Tercera edad (mas de 65 años)")
print("Total tercera edad")
print(len(df_tercera_edad))
print("Promedio tercera edad feliz")
print(len(df_tercera_edad_felices)/len(df_tercera_edad))

print("felicidad por edad y sexo")
resultados_edad_sexo = []
for edad in range(18, 24):
	for codigo_sexo, nombre_sexo in [(1, "Hombres"), (2, "Mujeres")]:
		grupo = df_bogota[(df_bogota["P6040"] == edad) & (df_bogota["P6020"] == codigo_sexo)]
		grupo_feliz = grupo[grupo["P1895"] >= 8]
		promedio = len(grupo_feliz) / len(grupo) if len(grupo) > 0 else 0
		resultados_edad_sexo.append({
			"Edad": edad,
			"Sexo": nombre_sexo,
			"Total": len(grupo),
			"Felices": len(grupo_feliz),
			"Promedio de felicidad (%)": round(promedio * 100, 2)
		})

tabla_edad_sexo = pd.DataFrame(resultados_edad_sexo)
print(tabla_edad_sexo.to_string(index=False))
