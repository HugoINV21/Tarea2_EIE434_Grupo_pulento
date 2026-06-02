# TAREA N°2 – SIMULADOR MUNDIALISTA CON POO Y PANDAS

**Integrantes:** Hugo Nuñez, Sebastian Palacios, Javiera Vega, Jordan Porras  

## Descripción

Programa en Python que simula una selección de fútbol candidata a campeona del mundo. Aplica Programación Orientada a Objetos (herencia, polimorfismo) y usa Pandas para crear un DataFrame, calcular estadísticas y exportar a CSV.

Selección elegida: **Argentina** (campeona del mundo 2022, base sólida + jóvenes promesas, firme candidata para 2026).

## Estructura del proyecto

```
tarea_mundial_poo/
├── main.py
├── jugadores.py
└── output/
    └── titulares_argentina.csv
```

## Conceptos de POO usados

- **Clase y objetos**: `Jugador` es la plantilla; cada jugador es un objeto.
- **Herencia**: `Portero`, `Defensa`, `Mediocampista`, `Delantero` heredan de `Jugador`.
- **Polimorfismo**: El método `mostrar_rol()` se redefine en cada clase hija. Al recorrer la lista de jugadores e invocar el método, cada uno responde con su posición.
- **Encapsulamiento (básico)**: Cada objeto guarda su estado (ej. `esta_lesionado`).

## Ejecución

1. Tener Python 3 y Pandas instalado (`pip install pandas`).
2. En la terminal, dentro de la carpeta del proyecto: `python main.py`

El programa muestra en pantalla:
- Acciones en la cancha (correr, atajar, patear, etc.)
- Roles de todos los jugadores (polimorfismo)
- Tabla completa del equipo
- Edad promedio, altura máxima
- Cantidad de jugadores por posición y promedio de edad por posición

Además, exporta un archivo `output/titulares_argentina.csv`.

## Explicación de los archivos

**`jugadores.py`**  
Contiene la clase padre `Jugador` (atributos: nombre, edad, altura, dorsal, esta_lesionado; métodos: correr, mostrar_rol, lesionar, recuperar).  
Clases hijas:
- `Portero`: atajar, sacar_balon. `mostrar_rol()` retorna "Soy portero"
- `Defensa`: marcar, barrerse. → "Soy defensa"
- `Mediocampista`: dar_pase_largo, dar_pase_corto. → "Soy mediocampista"
- `Delantero`: patear_al_arco, celebrar_gol. → "Soy delantero"

**`main.py`**  
- Importa las clases.
- Crea 11 jugadores (1 portero, 4 defensas, 4 mediocampistas, 2 delanteros).
- Demuestra métodos heredados, propios y polimorfismo.
- Construye un DataFrame con columnas: Pais, Dorsal, Nombre, Edad, Altura_m, Posicion.
- Calcula estadísticas pedidas y guarda CSV en `output/`.

## Ejemplo de salida (resumido)

```
--- SIMULADOR DE CAMPEÓN DEL MUNDO ---
Acciones en la cancha:
Emiliano Martinez está corriendo...
Emiliano Martinez realizó una atajada.
...
Roles del equipo:
Emiliano Martinez - Soy portero
Nahuel Molina - Soy defensa
...
[Estadísticas y CSV generado]
```

## Por qué Argentina es candidata

Argentina ganó el Mundial 2022, mantiene experiencia (Messi, Otamendi) y suma jóvenes (Enzo Fernández, Julián Álvarez). Buen funcionamiento colectivo y solidez defensiva. Con buen recambio, puede repetir el título en 2026.