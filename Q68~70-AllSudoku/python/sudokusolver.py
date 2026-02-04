from copy import deepcopy
from enum import Enum
from random import shuffle
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

        for value in list(candidates):
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
