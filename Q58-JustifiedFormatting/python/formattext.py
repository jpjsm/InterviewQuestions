from typing import List


class TextFormatter:
    def __init__(self, lines_page: int, line_width: int):
        if not isinstance(lines_page, int) or lines_page < 1:
            raise ValueError("Argument 'lines_page' must be a positive integer.")

        if not isinstance(line_width, int) or line_width < 1:
            raise ValueError("Argument 'line_width' must be a positive integer.")

        self.LinesPerPage: int = lines_page
        self.CharsPerLine: int = line_width
        self._paragraphs: List[str] = []

    def AddParagraphs(self, paragraphs: List[str]):
        if not isinstance(paragraphs, (list, tuple)):
            if not isinstance(paragraphs, str):
                raise ValueError("Argument 'paragraphs' must be a list of strings.")
            self._paragraphs.append(paragraphs)

        elif not all(isinstance(p, str) for p in paragraphs):
            raise ValueError("All items of 'paragraphs' must be of type string.")

        self._paragraphs += paragraphs

    def FormatJustified(self) -> List[str]:
        content: List[str] = []
        line: List[str] = []

        for paragraph in self._paragraphs:
            # A line is a list of words and spacings (one or more spaces
            # between words)
            line = []
            words = paragraph.split()
            current_length = 0
            current_spaces = 0
            for word in words:
                word_len = len(word)
                if not line:
                    line.append(word)
                    current_length = word_len
                elif current_length + 1 + word_len <= self.CharsPerLine:
                    # word fits in line
                    line.append(word)
                    current_spaces += 1
                    current_length += 1 + word_len
                else:
                    # word must go in next line
                    # adjust spacings until line is of desired length
                    spaces_to_redistribute = (
                        self.CharsPerLine - current_length
                    ) + current_spaces
                    base_spacing_len, remaining_spacing = divmod(
                        spaces_to_redistribute, current_spaces
                    )
                    base_spacing = " " * base_spacing_len
                    extra_spacing = base_spacing + " "
                    for i in range(current_spaces):
                        line.insert(
                            2 * i + 1,  # Spaces are always in odd numbered items
                            # small spacing to the left (smaller numbers)
                            # extra spacing to the right (larger numbers)
                            (
                                base_spacing
                                if i < current_spaces - remaining_spacing
                                else extra_spacing
                            ),
                        )

                    content.append("".join(line))
                    line = [word]
                    current_length = len(word)
                    current_spaces = 0
        # Check last line still in buffer
        if line:
            content.append(" ".join(line))  # last line is always Left Justified

        return content


if __name__ == "__main__":
    with open("./paragraph.txt", "r", encoding="utf-8") as infile:
        paragraph = infile.read()

    with open(
        "./justified_paragraph.txt", "r", encoding="utf-8", newline=None
    ) as infile:
        expected_lines = [line[:-1] for line in infile.readlines()]

    textformatter = TextFormatter(24, 64)
    textformatter.AddParagraphs([paragraph])
    r = textformatter.FormatJustified()
    if len(r) != len(expected_lines):
        print(
            f"Result number of lines {len(r)} != "
            f"{len(expected_lines)} number of expected lines"
        )
    for i in range(len(r)):
        if r[i] != expected_lines[i]:
            print(
                f"Line: {i} differences\n\tResult '{r[i]}' != "
                f"'{expected_lines[i]}' expected."
            )
            print(
                f"\tResult length {len(r[i])} {"==" if len(r) == len(expected_lines[i]) else "!="} {len(expected_lines[i])} expected length"
            )
            max_len = max(len(r[i]), len(expected_lines[i]))
            min_len = min(len(r[i]), len(expected_lines[i]))
            for j in range(min_len):
                if r[i][j] != expected_lines[i][j]:
                    print(
                        f"\tline [{i}] differs at char position {j}: {r[i][j]} != {expected_lines[i][j]}"
                    )
    print("Tests completed.")
