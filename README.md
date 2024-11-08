# Conway's Game of Life

A Python implementation of Conway's Game of Life, a cellular automaton devised by mathematician John Conway.

## About the Project

Conway's Game of Life is a zero-player game that simulates the life and death of cells on a two-dimensional grid based on simple rules. This project includes functions for initializing the grid, calculating cell states, and generating successive generations.

### Rules of the Game

1. Any live cell with two or three live neighbors survives.
2. Any dead cell with exactly three live neighbors becomes a live cell.
3. All other live cells die in the next generation, and all other dead cells stay dead.

## Project Structure

- `main.py`: The main file to run the simulation.
- `game_of_life.py`: Contains the core logic for calculating the next generation of cells.
- `constants.py`: Defines constants, such as grid size and symbols for alive and dead cells.
- `utils.py`: Utility functions, like pausing between generations for a smoother display.
- `README.md`: Project documentation.
- `requirements.txt`: Lists Python version requirements.

## Requirements

- **Python**: Version 3.10 or higher

All dependencies are part of Python's standard library, so no additional packages are required.

## Installation and Running

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/YourUsername/ConwaysGameOfLife.git
cd ConwaysGameOfLife
```

### 2. (Optional) Create a Virtual Environment

To keep dependencies isolated, you may want to use a virtual environment:

```bash
python3.10 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Requirements

Install the requirements specified in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Run the Simulation

To start the simulation, run:

```bash
python main.py
```

The program will display successive generations of cells according to the rules of Conway's Game of Life. Press `Ctrl-C` to exit.

## Example Output

Example interaction with the program:

```
Conway's Game of Life. Press Ctrl-C to quit.

 O    O
 O    O
 OOO OOO
```

This display will change with each generation as cells live and die according to the rules.

## License

This project is open-source and available under the MIT License.
