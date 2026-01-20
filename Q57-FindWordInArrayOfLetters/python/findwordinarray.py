import keyword
from typing import Dict, List, Set, Tuple


class LettersSoup:
    def __init__(self, letters_soup: List[str]):
        if not isinstance(letters_soup, (list, tuple)) or any(
            not isinstance(row, str) for row in letters_soup
        ):
            raise ValueError(f"'letters_soup' must be an array of strings")
        if not all(len(row) == len(letters_soup[0]) for row in letters_soup):
            raise ValueError(
                f"All strings in 'letters_soup' must be of the same length"
            )

        self._letters_soup: List[str] = letters_soup
        self._letters_map: Dict[str, List[Tuple[int, int]]] = {}

        for row in range(len(self._letters_soup)):
            for column in range(len(self._letters_soup[row])):
                letter = self._letters_soup[row][column]
                if letter not in self._letters_map:
                    self._letters_map[letter] = []
                self._letters_map[letter].append((row, column))

    @property
    def LettersMap(self) -> Dict[str, List[Tuple[int, int]]]:
        return self._letters_map

    def __str__(self) -> str:
        return "\n".join(" ".join(row) for row in self._letters_soup)

    def FindWordInArray(self, word: str) -> Tuple[bool, List[List[Tuple[int, int]]]]:
        def GetPossibleMoves(
            letters_soup: List[str], current_position: Tuple[int, int]
        ) -> List[Tuple[int, int]]:
            current_row, current_col = current_position
            candidatepositions: List[Tuple[int, int]] = []
            # Up
            up_row = current_row - 1
            if up_row >= 0:
                candidatepositions.append((up_row, current_col))
            # Down
            down_row = current_row + 1
            if down_row < len(letters_soup):
                candidatepositions.append((down_row, current_col))
            # Left
            left_col = current_col - 1
            if left_col >= 0:
                candidatepositions.append((current_row, left_col))
            # Right
            right_col = current_col + 1
            if right_col < len(letters_soup[current_row]):
                candidatepositions.append((current_row, right_col))

            return candidatepositions

        def GoNextLetter(
            letters_soup: List[str],
            word: str,
            current_position: Tuple[int, int],
            used_locations: Set[Tuple[int, int]],
        ) -> Tuple[bool, List[List[Tuple[int, int]]]]:
            if len(word) == 0:
                return (True, [])

            candidatepositions = GetPossibleMoves(letters_soup, current_position)
            results = []
            found = False
            target_letter = word[0]
            for pos in candidatepositions:
                if pos in used_locations:
                    # cannot used a used letter
                    continue
                next_row, next_col = pos
                next_letter = letters_soup[next_row][next_col]
                if target_letter == next_letter:
                    OK, paths = GoNextLetter(
                        letters_soup, word[1:], pos, used_locations.union([pos])
                    )  #  adding 'pos' to set of used_locations
                    if not OK:
                        return (False, [])

                    if not paths:
                        results.append([pos])
                    else:
                        for i in range(len(paths)):
                            paths[i].insert(0, pos)
                            results.append(paths[i])

                    used_locations.add(pos)
                    found = True

            return (found, results if found else [])

        _word = word.upper()
        initial_letter = _word[0]

        found = False
        solutions = []
        for initial_position in self.LettersMap[initial_letter]:
            OK, positions = GoNextLetter(
                self._letters_soup, _word[1:], initial_position, {initial_position}
            )
            if OK:
                found = True
                for i in range(len(positions)):
                    positions[i].insert(0, initial_position)

                solutions += positions

        return (found, solutions)


if __name__ == "__main__":
    letters_array = [
        "RPLISCTKGARYHFUGYYYREKKJAYBVAO",
        "AUHQZGJJASHJLBVEDBKVZXKWAXDQAY",
        "PEOVSOYHJKRTMJLNINRVPOFVYLVOHO",
        "SGOBYHJEAGZOTDYKTWFVNNEXAJSQAA",
        "EGZVHVTBBPRORTOLRJWTVCYBXKSLBP",
        "GSOAWVVEZLDDDUBTIYNFOUKGZUHJWB",
        "XYKIDXXEMBHFJQAJKDXZCWEZCFYOKB",
        "XDPYSAIXLVGZLNKSGHUJQFMJYOWETL",
        "WCRMZRHGDWHHWYVFGZUADMVVEYWPSO",
        "RASFMTMVCEGDLZGVGQXGRJJLHBGLZN",
        "SBPNMIGTNRTRAEOTRRPTSPWWRUJEYT",
        "DDQKDAGTPTJXXGPURBWPETUXXPIZFB",
        "YWIMWWTUYFXIHJLRZSCIETVUSPKAXY",
        "KYODUAZYJAEPDMQIIBILXZFXTJHFNZ",
        "YWBXQIAIWBETNABYGZSMQXPDBNFZHS",
    ]

    lettersoup = LettersSoup(letters_array)
    print(lettersoup)
    print()
    for k in sorted(lettersoup.LettersMap.keys()):
        print(f"'{k}' -> {lettersoup.LettersMap[k]}")

    tests = [("RPUHOVBY", True), ("ABCDEFG", False), ("HW", True)]

    for word, e in tests:
        r_OK, solutions = lettersoup.FindWordInArray(word)
        if r_OK != e:
            print(f"UnExpected r: {r_OK} != {e}")
        else:
            print(f"Target word: '{word}'")
            if r_OK:
                i = 0
                for solution in solutions:
                    print(
                        f"    Solution {i+1}: {[letters_array[row][col] for  (row, col) in solution]}"
                    )
                    print(f"    Solution {i+1}: {solution}")
                    i += 1
                print()
            else:
                print("    Target word not found, as expected.")

    print("Tests completed")

    key_words = keyword.kwlist
    key_words_in_soup = []
    key_words_not_in_soup = []
    for key_word in key_words:
        OK, solutions = lettersoup.FindWordInArray(key_word)
        if OK:
            key_words_in_soup.append(key_word)
        else:
            key_words_not_in_soup.append(key_word)

    print(f"Python keywords IN soup    : {key_words_in_soup}")
    print(f"Python keywords NOT in soup: {key_words_not_in_soup}")
