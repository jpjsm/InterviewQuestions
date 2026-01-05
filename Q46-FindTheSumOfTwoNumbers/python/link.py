from __future__ import annotations  # Enables forward references without quotes
from typing import Set


VALID_DIGITS: Set[str] = set(str(i) for i in range(10))
ZERO: str = "0"


class DigitLink:
    def __init__(self, value: str | None, next: DigitLink | None = None) -> None:
        if value is not None and value not in VALID_DIGITS:
            raise ValueError(f"'{value}' not in valid digits: {VALID_DIGITS}")
        self.Value = value
        self.Next = next if value else None

    @staticmethod
    def Add(a: DigitLink, b: DigitLink) -> DigitLink:
        a_link = a
        b_link = b
        carry: bool = False
        result = DigitLink(None)
        r_link = result
        previous: DigitLink | None = None
        while a_link and b_link:
            a_val = ord(a_link.Value) - ord(ZERO)
            b_val = ord(b_link.Value) - ord(ZERO)
            r_val = a_val + b_val + (1 if carry else 0)
            if r_val > 9:
                r_val = r_val - 10
                carry = True
            else:
                carry = False
            r_link.Value = str(r_val)
            r_link.Next = DigitLink(None)
            previous = r_link
            a_link = a_link.Next
            b_link = b_link.Next
            r_link = r_link.Next

        if a_link:
            while a_link:
                a_val = ord(a_link.Value) - ord(ZERO)
                r_val = a_val + (1 if carry else 0)
                if r_val > 9:
                    r_val = r_val - 10
                    carry = True
                else:
                    carry = False
                r_link.Value = str(r_val)
                r_link.Next = DigitLink(None)
                previous = r_link
                a_link = a_link.Next
                r_link = r_link.Next

        else:
            while b_link:
                b_val = ord(b_link.Value) - ord(ZERO)
                r_val = b_val + (1 if carry else 0)
                if r_val > 9:
                    r_val = r_val - 10
                    carry = True
                else:
                    carry = False
                r_link.Value = str(r_val)
                r_link.Next = DigitLink(None)
                previous = r_link
                b_link = b_link.Next
                r_link = r_link.Next

        if carry:
            r_link.Value = "1"
            r_link.Next = None
        else:
            if isinstance(previous, DigitLink):
                previous.Next = None

        return result


if __name__ == "__main__":
    a = DigitLink("9", DigitLink("9", DigitLink("9", DigitLink("9"))))
    b = DigitLink("2")
    c = DigitLink.Add(a, b)
    while c:
        print(c.Value)
        c = c.Next

    b = DigitLink("9", DigitLink("9", DigitLink("9", DigitLink("9"))))
    a = DigitLink("2")
    c = DigitLink.Add(a, b)
    while c:
        print(c.Value)
        c = c.Next
