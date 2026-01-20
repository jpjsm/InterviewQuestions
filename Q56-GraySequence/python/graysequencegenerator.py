from typing import List


def BitsOnCount(n: int) -> int:
    count = 0
    while n:
        n &= n - 1
        count += 1

    return count


def CheckGraySequence(sequence: List[int]) -> bool:
    for i in range(1, len(sequence)):
        if BitsOnCount(sequence[i] ^ sequence[i - 1]) != 1:
            return False
    return True


def GenerateGraySequence(bits: int) -> List[int]:
    if not isinstance(bits, int):
        raise ValueError("argument must be an integer.")

    if bits < 1:
        raise ValueError("argument must be a positive number")

    seq = [0, 1]
    left_bit = 1
    for _ in range(1, bits):
        tail = []
        left_bit <<= 1
        for i in range(len(seq)):
            k = len(seq) - 1 - i
            tail.append(left_bit | seq[k])

        seq += tail
    return seq


if __name__ == "__main__":
    tests = [(1, [0, 1]), (2, [0, 1, 3, 2]), (3, [0, 1, 3, 2, 6, 7, 5, 4])]
    for bits, expected in tests:
        result = GenerateGraySequence(bits)
        if len(expected) != len(result):
            print(f"Received result length '{len(result)}' != '{len(expected)}'")
        else:
            equal = True
            if not all(result[i] == expected[i] for i in range(len(result))):
                print(f"Received result: {result}' != {expected}")

    for bits in range(5, 9):
        seq = GenerateGraySequence(bits)
        if not CheckGraySequence(seq):
            print(f"Generated sequence for {bits} bits is not a Gray sequence.")
    print("Tests completed")
