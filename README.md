Juego de Sudoku 4x4 desarrollado en Python con interfaz de consola. El juego ofrece diferentes opciones de visualización, niveles de dificultad y un sistema de puntuación.
# Equipo de trabajo
- JHON FREDDY AGUIRRE CAÑON
- LIZETH KATHERINE TROCHEZ PAEZ
- FLOR ALBA TOVAR PEREA
- JOHAN SEBASTIAN ALONSO GUTIERREZ
- GERALDYN PAOLA PALACIO MARQUEZ
- YOVANY SORA OLAYA


## Características

- Tablero de 4x4 con números del 1 al 4
- Tres opciones de visualización:
  - Numérico (1-4)
  - Letras (A-D)
  - Símbolos (♣ ♦ ♥ ♠)
- Dos niveles de dificultad:
  - Fácil (6 casillas vacías)
  - Difícil (10 casillas vacías)
- Sistema de puntuación:
  - 10 puntos base por cada tablero resuelto
  - Bonus exponencial por victorias consecutivas
  - Registro de mejores puntajes

## Estructura del Proyecto

El proyecto está organizado en los siguientes archivos:

- `main.py`: Archivo principal que ejecuta el juego
- `sudoku_game.py`: Contiene la lógica principal del juego
- `sudoku_display.py`: Maneja las opciones de visualización
- `sudoku_difficulty.py`: Controla los niveles de dificultad
- `sudoku_score.py`: Gestiona el sistema de puntuación

## Requisitos

- Python 3.x

## Cómo Jugar

1. Ejecuta el juego:
   ```bash
   python main.py
   ```

2. En el menú principal, selecciona:
   - 1: Jugar
   - 2: Ver mejores puntajes
   - 3: Salir

3. Al seleccionar "Jugar":
   - Elige el tipo de visualización (1-3)
   - Selecciona el nivel de dificultad (1-2)
   - Ingresa tus movimientos en el formato: `fila columna valor`
     - Ejemplo: `1 2 3` (coloca el valor 3 en la fila 1, columna 2)
   - Para salir del juego actual, escribe `salir`

## Sistema de Puntuación

- 10 puntos base por cada tablero resuelto
- Bonus por victorias consecutivas:
  - Primera victoria: 10 puntos
  - Segunda victoria: 11 puntos (10 + 1)
  - Tercera victoria: 12 puntos (10 + 2)
  - Cuarta victoria: 14 puntos (10 + 4)
- Si pierdes, el contador de victorias consecutivas se reinicia a 0

## Mejores Puntajes

Los mejores puntajes se guardan en un archivo `highscores.json` y se muestran en orden descendente. Si logras un nuevo récord al salir del juego, se te pedirá tu nombre para registrarlo.

## Visualización del Tablero

- Nivel Fácil: Tablero encerrado en asteriscos (*)
- Nivel Difícil: Tablero encerrado en guiones (-)
