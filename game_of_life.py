"""Conway's Game of Life Logic.

This module contains the core logic for Conway's Game of Life, including
functions to initialize the grid, print the grid,
and calculate the next generation.
"""

import copy
import random
from constants import WIDTH, HEIGHT, ALIVE, DEAD


def initialize_grid():
    """Initialize the grid with random alive and dead cells."""
    grid = {}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            grid[(x, y)] = ALIVE if random.randint(0, 1) == 0 else DEAD
    return grid


def print_grid(grid):
    """Prints the current state of the grid to the console."""
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(grid[(x, y)], end='')
        print()


def get_next_generation(grid):
    """Calculate the next generation of cells based
       on Conway's Game of Life rules."""
    next_grid = copy.deepcopy(grid)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Calculate neighbors with wrapping
            neighbors = [
                grid[((x - 1) % WIDTH, (y - 1) % HEIGHT)],  # Top-left
                grid[(x, (y - 1) % HEIGHT)],                # Top
                grid[((x + 1) % WIDTH, (y - 1) % HEIGHT)],  # Top-right
                grid[((x - 1) % WIDTH, y)],                 # Left
                grid[((x + 1) % WIDTH, y)],                 # Right
                grid[((x - 1) % WIDTH, (y + 1) % HEIGHT)],  # Bottom-left
                grid[(x, (y + 1) % HEIGHT)],                # Bottom
                grid[((x + 1) % WIDTH, (y + 1) % HEIGHT)]   # Bottom-right
            ]
            num_alive_neighbors = neighbors.count(ALIVE)

            # Apply Conway's rules
            if grid[(x, y)] == ALIVE and num_alive_neighbors in [2, 3]:
                next_grid[(x, y)] = ALIVE
            elif grid[(x, y)] == DEAD and num_alive_neighbors == 3:
                next_grid[(x, y)] = ALIVE
            else:
                next_grid[(x, y)] = DEAD
    return next_grid
