import pandas as pd
import os

# Importamos las clases desde el archivo jugadores.py
from jugadores import Portero, Defensa, Mediocampista, Delantero

def main():
    # 1. Definimos el pais y creamos a los jugadores
    pais_elegido = 'Argentina'

    # Formacion obligatoria: 1 portero, 4 defensas, 4 mediocampistas, 2 delanteros
    p1 = Portero("Emiliano Martinez", 31, 1.95, 23, atajadas=85, penales=12)

    d1 = Defensa("Nahuel Molina", 26, 1.75, 26, balones_recuperados=40, despejes=30)
    d2 = Defensa("Cristian Romero", 25, 1.85, 13, balones_recuperados=60, despejes=45)
    d3 = Defensa("Nicolas Otamendi", 36, 1.83, 19, balones_recuperados=55, despejes=50)
    d4 = Defensa("Nicolas Tagliafico", 31, 1.72, 3, balones_recuperados=35, despejes=25)

    m1 = Mediocampista("Rodrigo De Paul", 29, 1.80, 7, asistencias=15, posesion=80)
    m2 = Mediocampista("Enzo Fernandez", 23, 1.78, 8, asistencias=10, posesion=85)
    m3 = Mediocampista("Alexis Mac Allister", 25, 1.74, 20, asistencias=12, posesion=82)
    m4 = Mediocampista("Angel Di Maria", 36, 1.80, 11, asistencias=25, posesion=75)

    del1 = Delantero("Lionel Messi", 36, 1.70, 10, goles=821, velocidad=80)
    del2 = Delantero("Julian Alvarez", 24, 1.70, 9, goles=35, velocidad=88)

    # Agrupamos a los 11 titulares en una lista
    jugadores_titulares = [p1, d1, d2, d3, d4, m1, m2, m3, m4, del1, del2]

    print("--- SIMULADOR DE CAMPEÓN DEL MUNDO ---")
    print(f"Selección elegida: {pais_elegido}\n")

    # 2. Demostrando las acciones en la cancha (metodos heredados y propios)
    print("Acciones en la cancha:")
    print(p1.correr())
    print(p1.atajar())
    print(del1.patear_al_arco())
    print(d2.barrerse())
    print(m1.dar_pase_largo())
    
    # Probando los metodos de la clase padre que cambian el estado del jugador
    print(del2.lesionar())
    print(del2.correr()) # Deberia decir que no puede correr
    print(del2.recuperar())

    # 3. Demostrando polimorfismo
    print("\nRoles del equipo:")
    for jug in jugadores_titulares:
        print(f"{jug.nombre} - {jug.mostrar_rol()}")

    # 4. Construccion del DataFrame con Pandas
    datos_equipo = []
    
    # Recorremos la lista para extraer los datos de cada objeto y armar el diccionario
    for j in jugadores_titulares:
        diccionario = {
            "Pais": pais_elegido,
            "Dorsal": j.dorsal,
            "Nombre": j.nombre,
            "Edad": j.edad,
            "Altura_m": j.altura,
            "Posicion": j.mostrar_rol()
        }
        datos_equipo.append(diccionario)

    df_equipo = pd.DataFrame(datos_equipo)

    print("\n--- ESTADÍSTICAS DEL EQUIPO ---")
    
    # Tabla completa
    print("\nTabla completa de titulares:")
    print(df_equipo.to_string())

    # Edad promedio
    edad_promedio = df_equipo["Edad"].mean()
    print(f"\nEdad promedio del plantel: {edad_promedio:.1f} años")

    # Altura maxima
    altura_max = df_equipo["Altura_m"].max()
    print(f"Altura máxima del equipo: {altura_max} m")

    # Cantidad de jugadores por posicion
    print("\nCantidad de jugadores por posición:")
    print(df_equipo["Posicion"].value_counts().to_string())

    # Promedio de edad por posicion
    print("\nPromedio de edad por posición:")
    promedios_edad = df_equipo.groupby("Posicion")["Edad"].mean()
    print(promedios_edad.to_string())

    # 5. Exportar a CSV
    # Verificamos si la carpeta output existe, si no, la creamos para que no tire error
    if not os.path.exists("output"):
        os.makedirs("output")

    ruta_csv = "output/titulares_argentina.csv"
    df_equipo.to_csv(ruta_csv, index=False)
    print(f"\nArchivo exportado exitosamente en: {ruta_csv}")

if __name__ == "__main__":
    main()