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

    def analyzer(
        empty_cells: List[Tuple[int, int]],
        availability: Dict[SudokuSections, List[Set[int]]],
    ) -> Optional[Dict[int, List[Tuple[int, int, Set[int]]]]]:
        results: Dict[int, List[Tuple[int, int, Set[int]]]] = {}

        for row, column in empty_cells:
            block = RC_to_block(row, column)
            candidate_solutions = (
                availability[SudokuSections.ROWS][row]
                & availability[SudokuSections.COLS][column]
                & availability[SudokuSections.BLOCKS][block]
            )
            if not candidate_solutions:
                # No solution available
                return None

            candidate_solutions_len = len(candidate_solutions)
            if candidate_solutions_len not in results:
                results[candidate_solutions_len] = []

            results[candidate_solutions_len].append((row, column, candidate_solutions))

        return results

    def solver_recursive(puzzle: List[List[int]]) -> Tuple[bool, List[List[int]]]:
        valid, availability, empty_cells = puzzlevalidator(puzzle)
        if not valid:
            raise ValueError("Invalid Puzzle")

        while empty_cells:
            analysis = analyzer(empty_cells, availability)
            if analysis is None:
                return (False, [])

            if 0 in analysis:
                raise ValueError(
                    f"The following cells are impossible to solve: {[(c[0], c[1]) for c in analysis[0]]}"
                )

            if 1 in analysis:
                for row, column, singleton in analysis[1]:
                    value = singleton.pop()
                    puzzle[row][column] = value

                valid, availability, empty_cells = puzzlevalidator(puzzle)
                if not valid:
                    return (False, [])

            else:
                for next_solution_level in sorted(
                    [k for k in analysis.keys() if k > 1]
                ):
                    for row, column, alternatives_set in analysis[next_solution_level]:
                        alternatives = sorted(alternatives_set)
                        for value in alternatives:
                            new_puzzle = deepcopy(puzzle)
                            new_puzzle[row][column] = value
                            solved, new_puzzle = solver_recursive(new_puzzle)
                            if solved:
                                return (solved, new_puzzle)

                return (False, [])

        return (True, puzzle)

    solved, solution = solver_recursive(puzzle)

    if not solved:
        raise ValueError("No Solution Found")

    return solution


if __name__ == "__main__":
    expected_solution = [
        [7, 8, 1, 3, 9, 5, 2, 4, 6],
        [9, 5, 6, 1, 2, 4, 3, 7, 8],
        [4, 2, 3, 8, 6, 7, 5, 9, 1],
        [3, 1, 8, 6, 7, 9, 4, 2, 5],
        [6, 7, 2, 5, 4, 1, 8, 3, 9],
        [5, 4, 9, 2, 8, 3, 6, 1, 7],
        [8, 9, 7, 4, 3, 6, 1, 5, 2],
        [1, 6, 4, 7, 5, 2, 9, 8, 3],
        [2, 3, 5, 9, 1, 8, 7, 6, 4],
    ]
    puzzles = [
        # [
        #     [7, 8, 1, 3, 9, 5, 2, 0, 0],
        #     [9, 0, 6, 1, 0, 4, 3, 7, 8],
        #     [0, 2, 3, 8, 0, 7, 5, 9, 1],
        #     [3, 1, 0, 0, 7, 9, 4, 2, 5],
        #     [6, 7, 2, 5, 4, 0, 8, 0, 9],
        #     [0, 4, 9, 2, 8, 3, 6, 0, 7],
        #     [0, 9, 7, 0, 0, 6, 1, 5, 2],
        #     [1, 0, 4, 7, 5, 2, 9, 8, 3],
        #     [2, 3, 5, 9, 1, 8, 7, 6, 0],
        # ],
        # [
        #     [7, 8, 0, 3, 9, 5, 0, 0, 6],
        #     [9, 5, 0, 0, 0, 4, 3, 7, 8],
        #     [4, 2, 3, 8, 6, 7, 0, 9, 1],
        #     [3, 0, 8, 6, 0, 9, 4, 0, 0],
        #     [6, 7, 0, 5, 4, 0, 8, 3, 0],
        #     [5, 4, 9, 2, 8, 3, 6, 1, 7],
        #     [0, 9, 7, 4, 0, 6, 1, 5, 2],
        #     [1, 0, 4, 7, 5, 2, 9, 8, 3],
        #     [2, 3, 5, 0, 1, 8, 0, 0, 0],
        # ],
        # [
        #     [0, 8, 0, 3, 0, 5, 2, 4, 0],
        #     [9, 5, 0, 0, 0, 4, 3, 7, 8],
        #     [4, 2, 3, 8, 6, 7, 0, 0, 1],
        #     [0, 1, 0, 6, 0, 0, 4, 2, 0],
        #     [0, 7, 0, 5, 4, 1, 8, 3, 9],
        #     [5, 4, 9, 2, 0, 3, 0, 0, 0],
        #     [0, 9, 7, 0, 3, 0, 0, 0, 2],
        #     [1, 0, 4, 7, 5, 2, 9, 8, 0],
        #     [2, 3, 0, 0, 0, 8, 7, 6, 4],
        # ],
        # [
        #     [0, 8, 0, 0, 9, 0, 2, 4, 6],
        #     [9, 0, 0, 1, 2, 4, 3, 0, 0],
        #     [4, 2, 0, 8, 0, 0, 5, 9, 0],
        #     [3, 1, 8, 0, 7, 0, 0, 2, 5],
        #     [6, 0, 2, 5, 4, 0, 8, 0, 0],
        #     [0, 4, 0, 0, 0, 3, 0, 1, 7],
        #     [8, 0, 7, 0, 0, 0, 1, 0, 2],
        #     [1, 6, 0, 7, 0, 2, 9, 0, 0],
        #     [0, 0, 0, 9, 1, 8, 0, 6, 4],
        # ],
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
    ]

    for puzzle in puzzles:
        solved, actual_solution = SudokuSolver(puzzle)
        if actual_solution != expected_solution:
            print("Houston we have a problem!")
            for _row in actual_solution:
                print("\t", _row)

            print(f"{'-'*40}\n")

    print("All puzzles evaluated")
