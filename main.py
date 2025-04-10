from creation import Window, Point, Line
from cell import Cell
from maze import Maze
import sys


def main():
    seed_input = input("Enter a seed number (or press Enter for random): ")

    if seed_input.strip():
        try:
            seed = int(seed_input)
        except ValueError:
            print("Invalid seed, using random seed instead.")
            seed = None
    else:
        seed = None


    print("Start of main", flush=True)
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    print("Setting recursion limit", flush=True)
    sys.setrecursionlimit(10000)

    print("Creating window", flush=True)
    win = Window(screen_x, screen_y)

    print("Creating maze", flush=True)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed)

    print("About to solve maze", flush=True)
    is_solvable = maze.solve()
    print("Maze solve returned", flush=True)

    if not is_solvable:
        print("maze can not be solved!", flush=True)
    else:
        print('maze solved!', flush=True)
    

    print("Waiting for window close", flush=True)
    win.wait_for_close()
    print("Window closed", flush=True)


if __name__ == "__main__":
    print("Program starting")
    main()
    print("Program ending")


