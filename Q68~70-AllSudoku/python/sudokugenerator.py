from copy import deepcopy
from enum import Enum
from random import shuffle, randint
from typing import Dict, List, Set, Tuple


class Levels(Enum):
    SOLUTION = 0
    BEGINNER = 2
    EASY = 3
    MEDIUM = 4
    HARD = 5


def GenerateSudoku(levels: Set[Levels] = set(Levels)) -> Dict[Levels, List[List[int]]]:
    BLOCKSIDE = 3
    SIZE = BLOCKSIDE * BLOCKSIDE
    CELLS_COUNT = SIZE * SIZE

    DIGITS = list(range(1, SIZE + 1))
    grid = [[0] * SIZE for _ in range(SIZE)]

    BLOCK2CELLBANDS: Dict[int, Tuple[int, int]] = {0: (0, 2), 1: (3, 5), 2: (6, 8)}
    available_rows: List[set[int]] = [set(DIGITS) for _ in range(SIZE)]
    available_cols: List[set[int]] = [set(DIGITS) for _ in range(SIZE)]
    available_blocks: List[set[int]] = [set(DIGITS) for _ in range(SIZE)]

    def CellToBRC(c: int) -> Tuple[int, int, int]:
        return (
            BLOCKSIDE * ((c // SIZE) // BLOCKSIDE) + ((c % SIZE) // BLOCKSIDE),
            *divmod(c, SIZE),
        )

    def _GenerateSudokuRecursive(
        cell_id: int,
    ) -> bool:

        if cell_id >= CELLS_COUNT:
            return True

        b, r, c = CellToBRC(cell_id)

        candidate_values = list(
            available_rows[r] & available_cols[c] & available_blocks[b]
        )
        if not candidate_values:
            return False

        shuffle(candidate_values)

        for candidate_value in candidate_values:
            grid[r][c] = candidate_value
            available_rows[r].remove(candidate_value)
            available_cols[c].remove(candidate_value)
            available_blocks[b].remove(candidate_value)
            # if IsLevelComplete():
            #     return True
            if _GenerateSudokuRecursive(cell_id + 1):
                return True

            grid[r][c] = 0
            available_rows[r].add(candidate_value)
            available_cols[c].add(candidate_value)
            available_blocks[b].add(candidate_value)

        return False

    def _Levelize(levels: Set[Levels] = set(Levels)) -> Dict[Levels, List[List[int]]]:
        sudokus: Dict[Levels, List[List[int]]] = {}
        for level in levels:
            level_grid = deepcopy(grid)
            remove_total = level.value
            for block in range(SIZE):
                r, c = divmod(block, BLOCKSIDE)
                for _ in range(remove_total):
                    level_grid[randint(*BLOCK2CELLBANDS[r])][
                        randint(*BLOCK2CELLBANDS[c])
                    ] = 0
            sudokus[level] = level_grid
        return sudokus

    success = _GenerateSudokuRecursive(cell_id=0)

    if not success:
        raise ValueError("[ERROR] Could Not Generate Puzzle")

    return _Levelize(levels)


if __name__ == "__main__":
    print("Begin Test Generate Sudoku")
    sudokus = GenerateSudoku()
    levels = sorted(sudokus.keys(), key=lambda l: l.value)

    for level in levels:
        sudoku = sudokus[level]
        print(f'{"-" * 10} Sudoku Puzzle: {level.name: ^9s}{"-" * 10}')
        for row in sudoku:
            # print("\t", row)
            print("\t", " ".join([" " if i == 0 else str(i) for i in row]))

    print(f'{"-" * 45}')
    print()
    print("End Test Generate Sudoku")
