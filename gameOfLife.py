import copy
import random
import time
import os

UPDATE_SPEED_SECONDS: float = 0.1
GRID_HEIGHT: int = 40
GRID_WIDTH: int = 40
EMPTY_CELL: str = " "
FULL_CELL: str = "#"


def create_grid() -> list:
    return [
        [FULL_CELL if random.randint(1, 5) == 1 else EMPTY_CELL for _ in range(GRID_WIDTH)]
        for _ in range(GRID_HEIGHT)
    ]


def print_grid(grid, generation_number) -> None:
    for cell in grid:
        print(" ".join(cell))

    print_generation_information(grid, generation_number)


def print_generation_information(grid, generation_number) -> None:
    print("generation_number:", generation_number)
    print("population:", count_all_cells(grid))
    print("--" * GRID_WIDTH)


def count_all_cells(grid) -> int:
    return sum(1 for row in grid for cell in row if cell == FULL_CELL)


def valid_neighbour(grid, row, column, head_cell_row, head_cell_column) -> bool:
    if not in_grid(row, column):
        return False

    return (row, column) != (head_cell_row, head_cell_column)

    return grid[row][column] != EMPTY_CELL


def in_grid(row, column) -> bool:
    if not (((row >= 0) and (row < GRID_HEIGHT)) and
            ((column >= 0) and (column < GRID_WIDTH))):
        return False
    return True


def update_cell(grid, temp_grid, row, column):
    neighbours_count = count_neighbours(temp_grid, row, column)
    if temp_grid[row][column] == FULL_CELL:
        update_full_cell(grid, row, column, neighbours_count)
    else:
        update_empty_cell(grid, row, column, neighbours_count)


def count_neighbours(grid, head_cell_row, head_cell_column) -> int:
    return sum(
        valid_neighbour(grid, row, column, head_cell_row, head_cell_column)
        for row in range(head_cell_row - 1, head_cell_row + 2)
        for column in range(head_cell_column - 1, head_cell_column + 2)
    )


def update_full_cell(grid, row, column, neighbours_count):
    if neighbours_count < 2 or neighbours_count > 3:
        grid[row][column] = EMPTY_CELL


def update_empty_cell(grid, row, column, neighbours_count):
    if neighbours_count == 3:
        grid[row][column] = FULL_CELL


def update_grid(grid) -> list:
    temporary_grid = copy.deepcopy(grid)

    for row in range(GRID_HEIGHT):
        for column in range(GRID_WIDTH):
            update_cell(grid, temporary_grid, row, column)

    return grid


def main_game_loop() -> None:
    generation_number: int = 0
    grid: list = create_grid()

    while True:
        print_grid(grid, generation_number)
        time.sleep(UPDATE_SPEED_SECONDS)
        os.system("clear")
        grid = update_grid(grid)

        generation_number += 1


if __name__ == "__main__":
    main_game_loop()
