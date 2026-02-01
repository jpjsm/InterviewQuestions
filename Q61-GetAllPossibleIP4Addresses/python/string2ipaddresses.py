from typing import List


def StringToIpAddresses(s: str) -> List[List[str]]:
    def getaddresses(s: str, l: int) -> List[List[str]]:
        if l == 0:
            if s == "" or len(s) > 3 or int(s) > 255:
                return []

            return [[s]]

        results = []
        for i in range(min(3, len(s))):
            left_s = s[: i + 1]
            right_s = s[i + 1 :]
            if int(left_s) > 255:
                continue
            right_segments = getaddresses(right_s, l - 1)
            if right_segments:
                for right_segment in right_segments:
                    results.append([left_s] + right_segment)

        return results

    if not isinstance(s,str) or s == "" or len(s) > 12 or not all(c >= "0" and c <= "9" for c in s):
        raise ValueError("Invalid argument")
    return getaddresses(s, 3)


if __name__ == "__main__":
    tests = [
        (
            "11111",
            [
                ["1", "1", "1", "11"],
                ["1", "1", "11", "1"],
                ["1", "11", "1", "1"],
                ["11", "1", "1", "1"],
            ],
        ),
        ("255255255255", [["255", "255", "255", "255"]]),
        ("333333333", []),
        (
            "19216801",
            [
                ["1", "92", "168", "01"],
                ["19", "2", "168", "01"],
                ["19", "21", "68", "01"],
                ["19", "216", "8", "01"],
                ["19", "216", "80", "1"],
                ["192", "1", "68", "01"],
                ["192", "16", "8", "01"],
                ["192", "16", "80", "1"],
                ["192", "168", "0", "1"],
            ],
        ),
        ("12121212", []),
    ]

    print("start tests")
    for s, e in tests:
        results = StringToIpAddresses(s)
        print((s, results))

    print("tests completed")
