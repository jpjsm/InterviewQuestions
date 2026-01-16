from typing import List


def FindFirstMissingInteger(numbers: List[int]) -> int:
    i = 0
    j = len(numbers) - 1
    N = i + 1
    while i <= j:
        if numbers[i] == N:
            # Number is in the right place, move to next
            i += 1
            N = i + 1
        elif numbers[i] < 1 or numbers[i] >= j:
            # swap with the number at the current end -> numbers[j]
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j -= 1
        else:
            while numbers[i] > N and numbers[i] <= j:
                t = numbers[i]
                numbers[t - 1], numbers[i] = numbers[i], numbers[t - 1]
    return N


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4, 5], 6),
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([1, 2, 3, 4, 9], 5),
        ([4, 3, 2, 1, 0, -1, 5], 6),
        ([4, 8, 2, 1, 0, -1, 5], 3),
    ]
    for t, e in tests:
        r = FindFirstMissingInteger(t)
        if e != r:
            print(f"ERROR: expected {e} != {r} result")
    print("Tests completed!")
