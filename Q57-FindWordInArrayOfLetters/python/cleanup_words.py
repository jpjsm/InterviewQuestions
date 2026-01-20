import re
from typing import Any, Dict, List, Set

OXFORD_LINE_PATTERN = (
    r"^(?P<word>[A-Za-z-]+)\s+(\([a-z /]+\))?\s*(/?(?P<part>[a-z])\.?,?\s*)+$"
)
OXFORD_LINE_REGEX = re.compile(OXFORD_LINE_PATTERN)


def cleanup(lines: List[str]) -> Dict[str, Any]:
    results: Dict[str, List[str] | Set[str]] = {
        "words": [],
        "parts": set(),
        "no-match": [],
    }

    for line in lines:
        line = line.strip()
        if line == "":
            continue

        m = OXFORD_LINE_REGEX.match(line)
        if m:
            word = m.group("word").lower()
            results["words"].append(word)
            parts: Set[str] = {
                m.group("part") for m in OXFORD_LINE_REGEX.finditer(line)
            }
            results["parts"] |= parts
        else:
            results["no-match"].append(line)

    return results


if __name__ == "__main__":
    with open("./common_words.txt", "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    results: Dict[str, List[str]] = cleanup(lines)
    print(f"'Words' count: {len(results['words'])}")
    print(f"'Parts' count: {len(results['parts'])}")
    print(f"'No-Match' count: {len(results['no-match'])}")

    with open("./oxford_2k_common_words.txt", "w", encoding="utf-8") as outfile:
        outfile.writelines(f"{word}\n" for word in sorted(results["words"]))
