from math import log
from secrets import randbelow


def get_base_for_url(total_cases: int = 4_294_967_296, max_chars: int = 6) -> int:
    base = 64
    for i in range(64, 1, -1):
        chars = int(log(total_cases, i)) + 1
        if chars > max_chars:
            return base
        base = i

    return -1


def int_to_base(num: int, base: int) -> str:
    """
    Convert an integer to a string in the given base (2 to 64).

    Supports negative numbers and zero.
    Base 64 uses: 0-9, A-Z, a-z, +, /
    """
    # Validate base range
    if not (2 <= base <= 64):
        raise ValueError("Base must be between 2 and 64.")

    # Digit characters for bases up to 64
    digits = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+_"

    # Handle zero explicitly
    if num == 0:
        return digits[0]

    # Handle negative numbers
    negative = num < 0
    num = abs(num)

    result = []
    while num > 0:
        num, rem = divmod(num, base)
        result.append(digits[rem])

    # Reverse to get correct order
    result_str = "".join(reversed(result))

    return "-" + result_str if negative else result_str


def short_url_generator(total_cases: int = 4_294_967_296, base: int = 52) -> str:
    return int_to_base(randbelow(total_cases), base)


# Example usage:
if __name__ == "__main__":
    max_cases = 4_294_967_296
    max_encoding_length = 6
    base_for_encoding = get_base_for_url(max_cases, max_encoding_length)
    encoded_url = short_url_generator(max_cases, base_for_encoding)
    print(f"{max_cases=}, {max_encoding_length=}, {base_for_encoding=}, {encoded_url=}")
