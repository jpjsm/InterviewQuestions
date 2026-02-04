from copy import deepcopy
from enum import Enum
from typing import Dict, List, Optional, Set, Tuple


class SudokuSections(Enum):
    ROWS = 1
    COLS = 2
    BLOCKS = 4


def SudokuSolver(puzzle: List[List[int]]) -> List[List[int]]:
    BLOCKSIDE = 3
    SIZE = BLOCKSIDE * BLOCKSIDE
    CELLS_COUNT = SIZE * SIZE

    DIGITS = set(range(1, SIZE + 1))

    def RC_to_block(row: int, column: int) -> int:
        return (row // BLOCKSIDE) * BLOCKSIDE + column // BLOCKSIDE

    def cell_to_BRC(cell: int) -> Tuple[int, int, int]:
        return (
            BLOCKSIDE * ((cell // SIZE) // BLOCKSIDE) + ((cell % SIZE) // BLOCKSIDE),
            *divmod(cell, SIZE),
        )

    def puzzlevalidator(
        puzzle: List[List[int]],
    ) -> Tuple[bool, Dict[SudokuSections, List[set[int]]], List[Tuple[int, int]]]:
        is_list = isinstance(puzzle, list)
        len_puzzle = len(puzzle)
        all_rows_are_list_len_9 = all(
            [isinstance(r, list) and len(r) == 9 for r in puzzle]
        )
        all_rows_values_in_valid_range = all(
            [isinstance(c, int) and (0 <= c <= 9) for r in puzzle for c in r]
        )
        if (
            not is_list
            or len_puzzle != 9
            or not all_rows_are_list_len_9
            or not all_rows_values_in_valid_range
        ):
            return (False, {}, [])

        output_availability = {
            section: [set(DIGITS) for _ in range(SIZE)] for section in SudokuSections
        }
        output_empty_cells = []

        for cell in range(CELLS_COUNT):
            block, row, column = cell_to_BRC(cell)
            value: int = puzzle[row][column]
            if value:
                if (
                    (value not in output_availability[SudokuSections.ROWS][row])
                    or (value not in output_availability[SudokuSections.COLS][column])
                    or (value not in output_availability[SudokuSections.BLOCKS][block])
                ):
                    output_availability = {}
                    output_empty_cells = []
                    return (False, output_availability, output_empty_cells)

                output_availability[SudokuSections.ROWS][row].remove(value)
                output_availability[SudokuSections.COLS][column].remove(value)
                output_availability[SudokuSections.BLOCKS][block].remove(value)

            else:
                output_empty_cells.append((row, column))

        return (True, output_availability, output_empty_cells)

    def place_value(
        row: int,
        column: int,
        value: int,
        availability: Dict[SudokuSections, List[Set[int]]],
    ):
        block = RC_to_block(row, column)
        availability[SudokuSections.ROWS][row].remove(value)
        availability[SudokuSections.COLS][column].remove(value)
        availability[SudokuSections.BLOCKS][block].remove(value)

    def remove_value(
        row: int,
        column: int,
        value: int,
        availability: Dict[SudokuSections, List[Set[int]]],
    ):
        block = RC_to_block(row, column)
        availability[SudokuSections.ROWS][row].add(value)
        availability[SudokuSections.COLS][column].add(value)
        availability[SudokuSections.BLOCKS][block].add(value)

    def select_cell(
        empty_cells: List[Tuple[int, int]],
        availability: Dict[SudokuSections, List[Set[int]]],
    ) -> Tuple[int, int, Set[int]]:
        best: Tuple[int, int, Set[int]] = (-1, -1, set())
        min_set_len = SIZE + 1

        for row, column in empty_cells:
            block = RC_to_block(row, column)
            candidates = (
                availability[SudokuSections.ROWS][row]
                & availability[SudokuSections.COLS][column]
                & availability[SudokuSections.BLOCKS][block]
            )

            if not candidates:
                return (-1, -1, set())

            if len(candidates) < min_set_len:
                min_set_len = len(candidates)
                best = (row, column, candidates)

        return best

    def solver_recursive(
        puzzle: List[List[int]],
        empty_cells: List[Tuple[int, int]],
        availability: Dict[SudokuSections, List[Set[int]]],
    ) -> bool:
        if not empty_cells:
            return True
        row, column, candidates = select_cell(empty_cells, availability)

        if not candidates:
            return False

        for value in list(candidates):  # sorted(candidates):
            puzzle[row][column] = value
            place_value(row, column, value, availability)
            empty_cells.remove((row, column))

            if solver_recursive(puzzle, empty_cells, availability):
                return True

            # Undo move (aka backtrack)
            puzzle[row][column] = 0
            remove_value(row, column, value, availability)
            empty_cells.append((row, column))

        return False

    valid, availability, empty_cells = puzzlevalidator(puzzle)
    if not valid:
        raise ValueError("Invalid Puzzle")

    solved = solver_recursive(puzzle, empty_cells, availability)

    if not solved:
        raise ValueError("No Solution Found")

    return puzzle


if __name__ == "__main__":
    tests = [
        (
            "Sudoku Generator: Beginner",
            [
                [7, 8, 1, 3, 9, 5, 2, 0, 0],
                [9, 0, 6, 1, 0, 4, 3, 7, 8],
                [0, 2, 3, 8, 0, 7, 5, 9, 1],
                [3, 1, 0, 0, 7, 9, 4, 2, 5],
                [6, 7, 2, 5, 4, 0, 8, 0, 9],
                [0, 4, 9, 2, 8, 3, 6, 0, 7],
                [0, 9, 7, 0, 0, 6, 1, 5, 2],
                [1, 0, 4, 7, 5, 2, 9, 8, 3],
                [2, 3, 5, 9, 1, 8, 7, 6, 0],
            ],
            [
                [7, 8, 1, 3, 9, 5, 2, 4, 6],
                [9, 5, 6, 1, 2, 4, 3, 7, 8],
                [4, 2, 3, 8, 6, 7, 5, 9, 1],
                [3, 1, 8, 6, 7, 9, 4, 2, 5],
                [6, 7, 2, 5, 4, 1, 8, 3, 9],
                [5, 4, 9, 2, 8, 3, 6, 1, 7],
                [8, 9, 7, 4, 3, 6, 1, 5, 2],
                [1, 6, 4, 7, 5, 2, 9, 8, 3],
                [2, 3, 5, 9, 1, 8, 7, 6, 4],
            ],
        ),
        (
            "Sudoku Generator: Easy",
            [
                [7, 8, 0, 3, 9, 5, 0, 0, 6],
                [9, 5, 0, 0, 0, 4, 3, 7, 8],
                [4, 2, 3, 8, 6, 7, 0, 9, 1],
                [3, 0, 8, 6, 0, 9, 4, 0, 0],
                [6, 7, 0, 5, 4, 0, 8, 3, 0],
                [5, 4, 9, 2, 8, 3, 6, 1, 7],
                [0, 9, 7, 4, 0, 6, 1, 5, 2],
                [1, 0, 4, 7, 5, 2, 9, 8, 3],
                [2, 3, 5, 0, 1, 8, 0, 0, 0],
            ],
            [
                [7, 8, 1, 3, 9, 5, 2, 4, 6],
                [9, 5, 6, 1, 2, 4, 3, 7, 8],
                [4, 2, 3, 8, 6, 7, 5, 9, 1],
                [3, 1, 8, 6, 7, 9, 4, 2, 5],
                [6, 7, 2, 5, 4, 1, 8, 3, 9],
                [5, 4, 9, 2, 8, 3, 6, 1, 7],
                [8, 9, 7, 4, 3, 6, 1, 5, 2],
                [1, 6, 4, 7, 5, 2, 9, 8, 3],
                [2, 3, 5, 9, 1, 8, 7, 6, 4],
            ],
        ),
        (
            "Sudoku Generator: Medium",
            [
                [0, 8, 0, 3, 0, 5, 2, 4, 0],
                [9, 5, 0, 0, 0, 4, 3, 7, 8],
                [4, 2, 3, 8, 6, 7, 0, 0, 1],
                [0, 1, 0, 6, 0, 0, 4, 2, 0],
                [0, 7, 0, 5, 4, 1, 8, 3, 9],
                [5, 4, 9, 2, 0, 3, 0, 0, 0],
                [0, 9, 7, 0, 3, 0, 0, 0, 2],
                [1, 0, 4, 7, 5, 2, 9, 8, 0],
                [2, 3, 0, 0, 0, 8, 7, 6, 4],
            ],
            [
                [7, 8, 1, 3, 9, 5, 2, 4, 6],
                [9, 5, 6, 1, 2, 4, 3, 7, 8],
                [4, 2, 3, 8, 6, 7, 5, 9, 1],
                [3, 1, 8, 6, 7, 9, 4, 2, 5],
                [6, 7, 2, 5, 4, 1, 8, 3, 9],
                [5, 4, 9, 2, 8, 3, 6, 1, 7],
                [8, 9, 7, 4, 3, 6, 1, 5, 2],
                [1, 6, 4, 7, 5, 2, 9, 8, 3],
                [2, 3, 5, 9, 1, 8, 7, 6, 4],
            ],
        ),
        (
            "Sudoku Generator: Hard",
            [
                [0, 8, 0, 0, 9, 0, 2, 4, 6],
                [9, 0, 0, 1, 2, 4, 3, 0, 0],
                [4, 2, 0, 8, 0, 0, 5, 9, 0],
                [3, 1, 8, 0, 7, 0, 0, 2, 5],
                [6, 0, 2, 5, 4, 0, 8, 0, 0],
                [0, 4, 0, 0, 0, 3, 0, 1, 7],
                [8, 0, 7, 0, 0, 0, 1, 0, 2],
                [1, 6, 0, 7, 0, 2, 9, 0, 0],
                [0, 0, 0, 9, 1, 8, 0, 6, 4],
            ],
            [
                [7, 8, 1, 3, 9, 5, 2, 4, 6],
                [9, 5, 6, 1, 2, 4, 3, 7, 8],
                [4, 2, 3, 8, 6, 7, 5, 9, 1],
                [3, 1, 8, 6, 7, 9, 4, 2, 5],
                [6, 7, 2, 5, 4, 1, 8, 3, 9],
                [5, 4, 9, 2, 8, 3, 6, 1, 7],
                [8, 9, 7, 4, 3, 6, 1, 5, 2],
                [1, 6, 4, 7, 5, 2, 9, 8, 3],
                [2, 3, 5, 9, 1, 8, 7, 6, 4],
            ],
        ),
        (
            "Arto Inkala: AI Escargot (2006)",
            [
                [1, 0, 0, 0, 0, 7, 0, 9, 0],
                [0, 3, 0, 0, 2, 0, 0, 0, 8],
                [0, 0, 9, 6, 0, 0, 5, 0, 0],
                [0, 0, 5, 3, 0, 0, 9, 0, 0],
                [0, 1, 0, 0, 8, 0, 0, 0, 2],
                [6, 0, 0, 0, 0, 4, 0, 0, 0],
                [3, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 4, 0, 0, 0, 0, 0, 0, 7],
                [0, 0, 7, 0, 0, 0, 3, 0, 0],
            ],
            [
                [1, 6, 2, 8, 5, 7, 4, 9, 3],
                [5, 3, 4, 1, 2, 9, 6, 7, 8],
                [7, 8, 9, 6, 4, 3, 5, 2, 1],
                [4, 7, 5, 3, 1, 2, 9, 8, 6],
                [9, 1, 3, 5, 8, 6, 7, 4, 2],
                [6, 2, 8, 7, 9, 4, 1, 3, 5],
                [3, 5, 6, 4, 7, 8, 2, 1, 9],
                [2, 4, 1, 9, 3, 5, 8, 6, 7],
                [8, 9, 7, 2, 6, 1, 3, 5, 4],
            ],
        ),
        (
            "Arto Inkala: Golden Nugget)",
            [
                [0, 2, 0, 0, 0, 0, 0, 0, 9],
                [0, 0, 0, 7, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 3, 0, 0, 0],
                [0, 0, 0, 5, 0, 7, 8, 0, 0],
                [5, 0, 0, 0, 0, 0, 0, 3, 0],
                [0, 0, 0, 0, 3, 4, 0, 6, 7],
                [0, 0, 5, 6, 0, 8, 0, 0, 0],
                [6, 0, 8, 0, 0, 0, 0, 4, 0],
                [0, 0, 0, 0, 0, 5, 6, 0, 0],
            ],
            [
                [7, 2, 6, 4, 5, 1, 3, 8, 9],
                [3, 5, 9, 7, 8, 6, 1, 2, 4],
                [4, 8, 1, 2, 9, 3, 7, 5, 6],
                [1, 4, 3, 5, 6, 7, 8, 9, 2],
                [5, 6, 7, 8, 2, 9, 4, 3, 1],
                [8, 9, 2, 1, 3, 4, 5, 6, 7],
                [9, 1, 5, 6, 4, 8, 2, 7, 3],
                [6, 7, 8, 3, 1, 2, 9, 4, 5],
                [2, 3, 4, 9, 7, 5, 6, 1, 8],
            ],
        ),
        (
            "Arto Inkala: Final Boss (2012)",
            [
                [8, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 3, 6, 0, 0, 0, 0, 0],
                [0, 7, 0, 0, 9, 0, 2, 0, 0],
                [0, 5, 0, 0, 0, 7, 0, 0, 0],
                [0, 0, 0, 0, 4, 5, 7, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 3, 0],
                [0, 0, 1, 0, 0, 0, 0, 6, 8],
                [0, 0, 8, 5, 0, 0, 0, 1, 0],
                [0, 9, 0, 0, 0, 0, 4, 0, 0],
            ],
            [
                [8, 1, 2, 7, 5, 3, 6, 4, 9],
                [9, 4, 3, 6, 8, 2, 1, 7, 5],
                [6, 7, 5, 4, 9, 1, 2, 8, 3],
                [1, 5, 4, 2, 3, 7, 8, 9, 6],
                [3, 6, 9, 8, 4, 5, 7, 2, 1],
                [2, 8, 7, 1, 6, 9, 5, 3, 4],
                [5, 2, 1, 9, 7, 4, 3, 6, 8],
                [4, 3, 8, 5, 2, 6, 9, 1, 7],
                [7, 9, 6, 3, 1, 8, 4, 5, 2],
            ],
        ),
        (
            "Arto Inkala: AI Escargot II (2009 ~ 2010)",
            [
                [0, 2, 3, 0, 0, 0, 7, 0, 0],
                [0, 0, 6, 0, 0, 0, 0, 0, 0],
                [7, 0, 0, 0, 2, 0, 4, 0, 6],
                [0, 0, 0, 0, 0, 0, 8, 0, 0],
                [0, 0, 7, 8, 0, 0, 2, 3, 4],
                [0, 0, 0, 0, 3, 4, 0, 6, 0],
                [0, 0, 0, 0, 7, 0, 0, 0, 2],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 6, 0, 0],
            ],
            [
                [1, 2, 3, 4, 6, 8, 7, 5, 9],
                [8, 4, 6, 7, 5, 9, 1, 2, 3],
                [7, 5, 9, 1, 2, 3, 4, 8, 6],
                [2, 3, 4, 6, 9, 7, 8, 1, 5],
                [9, 6, 7, 8, 1, 5, 2, 3, 4],
                [5, 8, 1, 2, 3, 4, 9, 6, 7],
                [6, 9, 8, 3, 7, 1, 5, 4, 2],
                [4, 7, 2, 5, 8, 6, 3, 9, 1],
                [3, 1, 5, 9, 4, 2, 6, 7, 8],
            ],
        ),
        (
            "Symmetries",
            [
                [1, 2, 3, 0, 0, 0, 0, 0, 0],
                [4, 5, 6, 0, 0, 0, 0, 0, 0],
                [7, 8, 9, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 2, 3, 0, 0, 0],
                [0, 0, 0, 4, 5, 6, 0, 0, 0],
                [0, 0, 0, 7, 8, 9, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 2, 3],
                [0, 0, 0, 0, 0, 0, 4, 5, 6],
                [0, 0, 0, 0, 0, 0, 7, 8, 9],
            ],
            [
                [1, 2, 3, 5, 6, 4, 8, 9, 7],
                [4, 5, 6, 8, 9, 7, 2, 3, 1],
                [7, 8, 9, 2, 3, 1, 5, 6, 4],
                [9, 7, 5, 1, 2, 3, 6, 4, 8],
                [3, 1, 8, 4, 5, 6, 9, 7, 2],
                [2, 6, 4, 7, 8, 9, 3, 1, 5],
                [5, 9, 7, 6, 4, 8, 1, 2, 3],
                [8, 3, 1, 9, 7, 2, 4, 5, 6],
                [6, 4, 2, 3, 1, 5, 7, 8, 9],
            ],
        ),
    ]

    print("Sudoku Solver - Begin tests")
    for name, puzzle, expected_solution in tests:
        print(f"{'=' * 15} {name} {'=' * 15}")
        actual_solution = SudokuSolver(puzzle)
        if actual_solution != expected_solution:
            print("Houston we have a problem!")
            for _row in actual_solution:
                print("\t", _row, ",")

            print(f"{'-'*40}\n")

    print("Sudoku Solver - Tests complete")
