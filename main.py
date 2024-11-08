"""Main file to run Conway's Game of Life."""

import sys
from game_of_life import initialize_grid, print_grid, get_next_generation
from utils import pause


def main():
    """Run the Conway's Game of Life simulation."""
    print("Conway's Game of Life. Press Ctrl-C to quit.")
    grid = initialize_grid()

    try:
        while True:
            print('\n' * 10)  # Clear the screen between generations
            print_grid(grid)
            grid = get_next_generation(grid)
            pause()
    except KeyboardInterrupt:
        print("\nConway's Game of Life simulation ended.")
        sys.exit()


if __name__ == "__main__":
    main()
