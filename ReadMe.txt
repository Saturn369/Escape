# Depths of the Unknown - Game README

## Overview
"Depths of the Unknown" is a terminal-based, grid exploration game where the player navigates through a mysterious and dangerous labyrinth filled with monsters, traps, and treasures. The objective is to survive each level by avoiding bombs, defeating monsters, and finding the exit to progress to the next stage.

## Gameplay Instructions

### Controls:
- **W**: Move Up
- **S**: Move Down
- **A**: Move Left
- **D**: Move Right

### Objective:
- **Survive**: Avoid traps (bombs), defeat monsters, and find the exit on each level to proceed.
- **Explore**: Discover hearts and mana to boost your health and magical abilities.

### Game Elements:
- **Player ('P')**: Your character in the game.
- **Monster ('M')**: A monster you may encounter and battle.
- **Visited ('X')**: Tiles you've already explored.
- **Unvisited ('.')**: Tiles you haven't explored yet.

### Encounters:
- **Fountain of Life**: Increases your health by 1.
- **Bomb**: Reduces your health by 1.
- **Exit**: Proceed to the next level.
- **Mana Source**: Increases your mana by 1.
- **Monster**: Engage in battle with randomized attack, defense, and health stats.

## Game Mechanics

### Player Stats:
- **Health**: Starts at 9. If it drops to 0, the game is over.
- **Mana**: Starts at 9. Used for magical abilities (though not yet implemented in this version).
- **Attack**: Determines how much damage you deal to monsters.
- **Defense**: Determines how much damage you can block from monsters.

### Monster Stats:
- **Attack**: Varies between 1 and 5.
- **Defense**: Varies between 1 and 5.
- **HP**: Varies between 5 and 10.

### Level Structure:
- The game consists of multiple levels, each with a 4x4 grid.
- The player's starting position is always the top-left corner of the grid.
- Each level includes a bomb, an exit, and potentially a monster, heart, or mana source.

### Combat:
- Combat alternates between the player's turn and the monster's turn.
- Both attack and defense are randomized each turn.
- Victory in combat results in progressing to explore the level further, while defeat results in a game over.

## Installation and Running the Game

### Prerequisites:
- Python 3.x
- Required libraries: `random`, `os`, `time`, `keyboard`, `threading`

### Running the Game:
1. **Clone or download the repository**.
2. **Install dependencies**:
   - Run `pip install keyboard` if the `keyboard` module is not already installed.
3. **Run the game**:
   - Navigate to the directory containing the script and execute `python <script_name>.py`.

### Known Issues:
- **High CPU Usage**: The game uses a continuous loop with a short sleep, which may result in higher CPU usage.

### Future Improvements:
- Implement mana-based abilities.
- Add more detailed levels with different grid sizes and obstacles.
- Introduce different types of monsters and power-ups.

## License
This game is free to play and modify. Attribution is appreciated but not required.

## Contribution
Feel free to fork the repository and contribute by submitting pull requests. Bug reports and feature suggestions are welcome!

Enjoy venturing into the Depths of the Unknown!