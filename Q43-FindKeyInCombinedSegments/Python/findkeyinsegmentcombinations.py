"""Find Key in Segments Combinations

Combine the items in the segments list, in pairs, to see if the key is contained
in any of those combinations; and return the combinations where the key is
found.

For example:

List: [ "12", "123", "312", "1412", "012", "4321" ]

Key: "1212"

Answer:

```txt
[
    (0, 1, "12123"),
    (2, 0, "31212"),
    (2, 1, "312123"),
    (3, 0, "141212"),
    (3, 1, "1412123"),
    (4, 0, "01212"),
    (4, 1, "012123"),
]
```
"""

from typing import List, Tuple


def FindKeyInSegmentCombinations(
    segments: List[str], key: str
) -> List[Tuple[int, int, str]]:
    segments_len = len(segments)
    results: List[Tuple[int, int, str]] = []
    for i in range(segments_len):
        for j in range(segments_len):
            if j == i:
                continue  # the segment cannot be combined with itself
            combination = segments[i] + segments[j]
            if key in combination:
                results.append((i, j, combination))

    return results


if __name__ == "__main__":
    results = FindKeyInSegmentCombinations(
        ["12", "123", "312", "1412", "012", "4321"], "1212"
    )
    for result in results:
        print(result)
