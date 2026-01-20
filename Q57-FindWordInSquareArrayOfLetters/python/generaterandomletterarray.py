import random
import string
from typing import List


def LettersSoup(rows: int, columns: int) -> List[str]:
    if not isinstance(rows, int) or not isinstance(columns, int):
        raise ValueError(
            "Number of rows and number of columns must both be of integer type"
        )

    if rows < 1 or columns < 0:
        raise ValueError(
            "Number of rows and number of columns must both be positive greater"
            " than zero."
        )

    arr = []
    for _ in range(rows):
        row = "".join(random.choice(string.ascii_uppercase) for _ in range(columns))
        arr.append(row)

    return arr


if __name__ == "__main__":
    letters_soup = LettersSoup(15, 30)
    for row in letters_soup:
        print(f"{' '.join(row)} ")
