# Python Go (Weiqi) Game

This is a simple implementation of the classic board game Go (also known as Weiqi or Baduk) using Python and Pygame. The game features a graphical user interface where two players can take turns placing stones on a 19x19 board.

## Features

- Full 19x19 Go board
- Two-player gameplay (Black: Dimi, White: Alice)
- Stone capture mechanics
- Score tracking
- Simple and clean user interface

## Requirements

- Python 3.6+
- Pygame
- NumPy

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/MonkWarrior08/Go-Weiqi-Game_Engine.git
   cd Go-Weiqi-Game_Engine
   ```

2. Install the required dependencies:
   ```
   pip install pygame numpy
   ```

## How to Play

1. Run the game:
   ```
   python go.py
   ```

2. The game window will open, showing the Go board.

3. Players take turns clicking on the board intersections to place their stones.
   - Black (Dimi) goes first
   - White (Alice) goes second

4. The game follows standard Go rules:
   - Capture opponent's stones by surrounding them
   - The game ends when both players pass consecutively
   - The player with the most territory and captured stones wins

5. The current player's turn and the score for each player are displayed on the screen.

6. Close the window to end the game.


## License

This project is open source and available under the [MIT License](LICENSE).

