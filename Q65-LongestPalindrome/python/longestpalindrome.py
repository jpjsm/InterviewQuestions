from random import choice, randint
import string
from typing import Dict, List, Tuple


def GeneratePalindromes(chars: str, length: int) -> str:
    result: List[str] = []
    if (length & 1) == 1:
        result.append(choice(chars))

    for _ in range(length >> 1):
        c = choice(chars)
        result.append(c)
        result.insert(0, c)
    return "".join(result)


def ReducePalindrome(palindrome: str, parts: int, new_chars: str = "") -> str:
    len_palindrome = len(palindrome)
    if len_palindrome < 2:
        return palindrome

    half_len = len_palindrome >> 1
    last_palindrome = len_palindrome - 1

    broken_palindrome: List[str] = list(palindrome)
    if parts < 1:
        for i in range(half_len):
            r = randint(half_len, last_palindrome)
            broken_palindrome[r], broken_palindrome[i] = (
                broken_palindrome[i],
                broken_palindrome[r],
            )
        return "".join(broken_palindrome)

    if new_chars:
        for i in range(parts):
            c = choice(new_chars)
            n = randint(0, last_palindrome)
            broken_palindrome[n] = c

        return "".join(broken_palindrome)

    for i in range(parts):
        left = randint(0, half_len)
        right = randint(half_len, last_palindrome)
        broken_palindrome[right], broken_palindrome[left] = (
            broken_palindrome[left],
            broken_palindrome[right],
        )

    return "".join(broken_palindrome)


def IsPalindrome(s: str) -> bool:
    # l = 0
    # r = len(s) - 1

    # while l <= r and s[l] == s[r]:
    #     l += 1
    #     r -= 1
    # return l > r
    return s == s[::-1]


def LongestPalindrome(s: str) -> str:
    letter_positions: Dict[str, List[int]] = {}
    for i in range(len(s)):
        l = s[i]
        if not l in letter_positions:
            letter_positions[l] = []

        letter_positions[l].append(i)

    longestpalindrome = ""

    for i in range(len(s)):
        if (len(s) - i) < len(longestpalindrome):
            break

        c = s[i]
        if len(letter_positions[c]) < 2:
            continue

        for right in reversed(letter_positions[c]):
            if right <= i or (right - i + 1) <= len(longestpalindrome):
                break

            if IsPalindrome(s[i : right + 1]):
                if len(s[i : right + 1]) > len(longestpalindrome):
                    longestpalindrome = s[i : right + 1]
                break

    return longestpalindrome


if __name__ == "__main__":
    # Generate palindromes
    # Valid palindromes are to be Uppercased letters
    test_is_palindrome = [
        ("OFGUIUGFO", True),
        ("OFGUIUGFOOFGUIUGFO", True),
        ("OFGUIUGFOOFGUIUGFOOFGUIUGFO", True),
        ("EvHZMZHJE", False),
        ("EJHZMZHJEjJHZMZHJE", False),
        ("EJHZMZHJEEJHZMZdJEEJHZMZHJE", False),
    ]
    for t, e in test_is_palindrome:
        r = IsPalindrome(t)
        if r != e:
            print(f"[ERROR] expected '{e}' != '{r}' result.")

    print("IsPalindrome Tests Completed")
    test_palindromes = [
        ("EvHZMZHJE", "HZMZH"),
        ("EJHZMZHJEjJHZMZHJE", "EJHZMZHJE"),
        ("EJHZMZHJEEJHZMZdJEEJHZMZHJE", "ZMZHJEEJHZMZ"),
        ("abacdfgdcaba", "aba"),
        ("abba", "abba"),
    ]

    for t, e in test_palindromes:
        r = LongestPalindrome(t)
        if r != e:
            print(f"[ERROR] expected '{e}' != '{r}' result.")

    print("Longest Palindromes Tests Completed")
