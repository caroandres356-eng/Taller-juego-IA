# 🎮 Triki (Tres en Línea) con Inteligencia Artificial

¡Bienvenido al proyecto **Triki** (también conocido como Tic-Tac-Toe o Tres en Línea)! 

Este proyecto es una implementación clásica del juego en Python, con una interfaz gráfica amigable desarrollada utilizando `tkinter`. 
El juego incluye una **Inteligencia Artificial (IA)** invencible contra la que puedes jugar, desarrollada como parte de la materia de **Introducción a la Inteligencia Artificial**.

## 👥 Equipo de Trabajo (Taller Juegos IA)
- Andrés Caro
- Mariana Grijalba
- Juan Murcia
- Sergio Clavijo

## ✨ Características Principales
- **Interfaz Gráfica de Usuario (GUI):** Tablero interactivo y fácil de usar.
- **Modos de Juego:** 
  - Jugar contra un amigo localmente (Jugador vs Jugador).
  - Jugar contra la máquina (Jugador vs IA).
- **Detección Automática:** Identifica inmediatamente si hay un ganador o si ocurre un empate.
- **Opción de Reinicio:** Reinicia la partida en cualquier momento desde el menú "Opciones".

---

## 🧠 ¿Cómo funciona nuestra Inteligencia Artificial?

La Inteligencia Artificial de este juego fue construida utilizando un algoritmo clásico llamado **Minimax**, el cual fue optimizado (hecho más rápido) usando una técnica llamada **Poda Alfa-Beta**. Aquí te explicamos de manera sencilla cómo funcionan:

### 1. El Algoritmo Minimax (Pensar en todas las posibilidades)
Imagina que estás jugando ajedrez y, antes de mover una pieza, piensas: *"Si muevo aquí, mi oponente moverá allá, y entonces yo podré mover allá..."*. 

El algoritmo Minimax hace exactamente eso, pero **para todas las jugadas posibles hasta el final del juego**. 
- Calcula un puntaje para cada posible final de partida: si la IA gana obtiene **+10 puntos**, si tú ganas ella obtiene **-10 puntos**, y si empatan son **0 puntos**.
- La IA siempre busca **maximizar** sus puntos (elegir el camino que le dé +10).
- Pero sabe que tú, como buen jugador, buscarás **minimizar** sus puntos (elegir el camino que le dé -10).

Sabiendo esto, la IA simula turnos de ambos jugadores en el tablero para tomar la decisión que le garantice, en el peor de los casos, un empate. ¡Por eso es imposible ganarle!

### 2. La Poda Alfa-Beta (Un atajo inteligente)
El problema de pensar en *todas* las jugadas posibles es que toma mucho tiempo y esfuerzo para el computador, incluso en un juego simple como el Triki.

Aquí entra la **Poda Alfa-Beta**. Básicamente es un "atajo mental" para la IA. 
Si la IA está evaluando una posible jugada y llega a la conclusión de que *"esta opción es malísima, el jugador me ganaría de inmediato"*, **deja de evaluar esa rama** (la "poda" como a un árbol) y pasa a evaluar otras jugadas. 

Esto hace que la IA no pierda tiempo pensando en jugadas que ya sabe que son perdedoras, volviéndose extremadamente **rápida y eficiente**.

---

## 💻 ¿Cómo funciona en nuestro código?
El proyecto se divide en módulos para mantener todo organizado:

1. **`main.py`**: Es el archivo principal. Al ejecutarlo, enciende la interfaz gráfica y comienza el juego.
2. **`ui.py`**: Maneja todo lo visual. Dibuja los botones, muestra las ventanas de "Ganaste" o "Empate" y, si seleccionas "Jugar Vs IA", se encarga de pedirle a la máquina que haga su jugada cuando es su turno (`ai_move()`). También se asegura de que tú no puedas hacer trampa haciendo clic cuando no es tu turno.
3. **`game.py`**: Conoce las reglas del juego. Sabe cómo verificar si alguien ha ganado (`check_winner`), si hay empate (`is_draw`) o si todavía quedan casillas vacías.
4. **`ai.py`**: Aquí vive el "cerebro" de la máquina. Contiene la función `minimax()` (que calcula las jugadas y aplica los atajos de la Poda Alfa-Beta) y `get_best_move()` (que le entrega a la interfaz la casilla exacta donde debe colocar el círculo rojo "O").

---

## 🚀 Cómo Ejecutar el Juego (Instrucciones)

Para jugar, solo necesitas **Python** instalado en tu computadora.

1. Abre una terminal o consola de comandos.
2. Navega hasta la carpeta `TRIKI` de este proyecto:
   ```bash
   cd "ruta/a/la/carpeta/Taller-juego-IA/TRIKI"
   ```
3. Ejecuta el archivo principal:
   ```bash
   python main.py
   ```
4. Se abrirá la ventana. Ve arriba a la izquierda, da clic en **Opciones** > **Jugar Vs IA** ¡y haz tu primer movimiento!
