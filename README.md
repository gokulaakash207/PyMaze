# PyMaze-game
A Python maze game using Pygame that generates perfect random mazes with DFS. Navigate a blue player through white paths while avoiding walls to reach the green goal. The game includes five levels, smooth movement, collision detection, and automatic level progression with new mazes each restart.

🧩 Maze Game (Python + Pygame)

A fun and challenging maze escape game built using Python and Pygame.
This project automatically generates 5 random perfect mazes, each serving as a new level.
Navigate the blue player through the maze and reach the green goal!

🚀 Features

🔹 Perfect Maze Generation using recursive backtracking

🔹 5 Levels, each pre-generated at the start

🔹 Smooth Player Movement (WASD / Arrow Keys)

🔹 Level Completion Screen

🔹 Automatic Level Load & Restart

🔹 Simple, fast, and fully offline

🎮 Controls

| Key        | Action                                 |
| ---------- | -------------------------------------- |
| ⬆️ / **W** | Move Up                                |
| ⬇️ / **S** | Move Down                              |
| ⬅️ / **A** | Move Left                              |
| ➡️ / **D** | Move Right                             |
| **SPACE**  | Next Level / Restart After Final Level |

🛠 Requirements

pip install pygame

▶️ How to Run

git clone https://github.com/Kabilan-A-S/PyMaze-game.git
cd PyMaze-game
python main.py

📁 Project Structure

maze-game/
PyMaze-game/

│-- main.py

│-- README.md

🧠 Maze Generation Logic

This game uses recursive backtracking to create a perfect maze:

Walls → 1

Paths → 0

Player starts at (1, 1)

Goal located at (rows - 2, cols - 2)

Each level is generated before the game starts to ensure smooth gameplay.






