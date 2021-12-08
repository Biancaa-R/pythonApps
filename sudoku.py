from typing import List, Optional, Tuple

Matrix = List[List[int]]

# assigning initial values to the grid
initial_grid: Matrix = [
    [3, 0, 6, 5, 1, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]

# a grid with no solution
no_solution: Matrix = [
    [5, 0, 6, 5, 0, 8, 4, 0, 3],
    [5, 2, 0, 0, 0, 0, 0, 0, 2],
    [1, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]


def is_safe(grid: Matrix, row: int, column: int, n: int) -> bool:
    """
    This function checks the grid to see if each row,
    column, and the 3x3 subgrids contain the digit 'n'.
    It returns False if it is not 'safe' (a duplicate digit
    is found) else returns True if it is 'safe'
    """
    for i in range(9):
        if grid[row][i] == n or grid[i][column] == n:
            return False

    for i in range(3):
        for j in range(3):
            if grid[(row - row % 3) + i][(column - column % 3) + j] == n:
                return False

    return True


def is_completed(grid: Matrix) -> bool:
    """
    This function checks if the puzzle is completed or not.
    it is completed when all the cells are assigned with a non-zero number.
    >>> is_completed([[0]])
    False
    >>> is_completed([[1]])
    True
    >>> is_completed([[1, 2], [0, 4]])
    False
    >>> is_completed([[1, 2], [3, 4]])
    True
    >>> is_completed(initial_grid)
    False
    >>> is_completed(no_solution)
    False
    """
    return all(all(cell != 0 for cell in row) for row in grid)


def find_empty_location(grid: Matrix) -> Optional[Tuple[int, int]]:
    """
    This function finds an empty location so that we can assign a number
    for that particular row and column.
    """
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None


def sudoku(grid: Matrix) -> Optional[Matrix]:
    """
    Takes a partially filled-in grid and attempts to assign values to
    all unassigned locations in such a way to meet the requirements
    for Sudoku solution (non-duplication across rows, columns, and boxes)
    >>> sudoku(initial_grid)  # doctest: +NORMALIZE_WHITESPACE
    [[3, 1, 6, 5, 7, 8, 4, 9, 2],
     [5, 2, 9, 1, 3, 4, 7, 6, 8],
     [4, 8, 7, 6, 2, 9, 5, 3, 1],
     [2, 6, 3, 4, 1, 5, 9, 8, 7],
     [9, 7, 4, 8, 6, 3, 1, 2, 5],
     [8, 5, 1, 7, 9, 2, 6, 4, 3],
     [1, 3, 8, 9, 4, 7, 2, 5, 6],
     [6, 9, 2, 3, 5, 1, 8, 7, 4],
     [7, 4, 5, 2, 8, 6, 3, 1, 9]]
     >>> sudoku(no_solution) is None
     True
    """

    if is_completed(grid):
        return grid

    location = find_empty_location(grid)
    if location is not None:
        row, column = location
    else:
        # If the location is ``None``, then the grid is solved.
        return grid

    for digit in range(1, 10):
        if is_safe(grid, row, column, digit):
            grid[row][column] = digit

            if sudoku(grid) is not None:
                return grid

            grid[row][column] = 0

    return None


def print_solution(grid: Matrix) -> None:
    """
    A function to print the solution in the form
    of a 9x9 grid
    """
    for row in grid:
        for cell in row:
            print(cell, end=" ")
        print()


if __name__ == "__main__":
    # make a copy of grid so that you can compare with the unmodified grid
    for example_grid in (initial_grid, no_solution):
        print("\nExample grid:\n" + "=" * 20)
        print_solution(example_grid)
        print("\nExample grid solution:")
        solution = sudoku(example_grid)
        if solution is not None:
            print_solution(solution)
        else:
            print("Cannot find a solution.")
