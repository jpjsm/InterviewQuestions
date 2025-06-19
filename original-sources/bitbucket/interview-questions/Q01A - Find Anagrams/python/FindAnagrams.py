#!/usr/bin/env python3
import sys
import os.path

letter_values = [
    ('EN', 'e', 2),
    ('EN', 't', 3),
    ('EN', 'a', 5),
    ('EN', 'o', 7),
    ('EN', 'i', 11),
    ('EN', 'n', 13),
    ('EN', 's', 17),
    ('EN', 'h', 19),
    ('EN', 'r', 23),
    ('EN', 'd', 29),
    ('EN', 'l', 31),
    ('EN', 'c', 37),
    ('EN', 'u', 41),
    ('EN', 'm', 43),
    ('EN', 'w', 47),
    ('EN', 'f', 53),
    ('EN', 'g', 59),
    ('EN', 'y', 61),
    ('EN', 'p', 67),
    ('EN', 'b', 71),
    ('EN', 'v', 73),
    ('EN', 'k', 79),
    ('EN', 'j', 83),
    ('EN', 'x', 89),
    ('EN', 'q', 97),
    ('EN', 'z', 101),
    ('ES', 'e', 2),
    ('ES', 'é', 2),
    ('ES', 'a', 3),
    ('ES', 'á', 3),
    ('ES', 'o', 5),
    ('ES', 'ó', 5),
    ('ES', 's', 7),
    ('ES', 'n', 11),
    ('ES', 'ñ', 103),
    ('ES', 'i', 13),
    ('ES', 'í', 13),
    ('ES', 'r', 17),
    ('ES', 'd', 19),
    ('ES', 'l', 23),
    ('ES', 't', 29),
    ('ES', 'c', 31),
    ('ES', 'm', 37),
    ('ES', 'u', 41),
    ('ES', 'ú', 41),
    ('ES', 'ü', 41),
    ('ES', 'p', 43),
    ('ES', 'b', 47),
    ('ES', 'g', 53),
    ('ES', 'v', 59),
    ('ES', 'y', 61),
    ('ES', 'q', 67),
    ('ES', 'h', 71),
    ('ES', 'f', 73),
    ('ES', 'j', 79),
    ('ES', 'z', 83),
    ('ES', 'x', 89),
    ('ES', 'w', 97),
    ('ES', 'k', 101)
]

letter_map = {}

for (lang, letter, value) in letter_values:
    lang = lang.upper()
    if lang not in letter_map:
        letter_map[lang] = {}

    letter_map[lang][letter] = value


words = [
    "AD",
    "BC",
    "Arches",
    "Golf",
    "Arcs",
    "Rats",
    "Arts",
    "Scar",
    "Bluest",
    "Search",
    "Bluets",
    "Star",
    "Bustle",
    "Sublet",
    "Cars",
    "Subtle",
    "Chaser",
    "Tars",
    "Tears"
]

def FindAnagrams1(words):
    anagrams_map = {}

    for word in words:
        key = ''.join(sorted(word.lower()))

        if  key not in anagrams_map:
            anagrams_map[key] = []

        anagrams_map[key].append(word)

    results = [(k, anagrams_map[k]) for k in anagrams_map if len(anagrams_map[k]) > 1]
    return results

def FindAnagrams2(words, lang):
    language = lang.upper()
    if language not in letter_map:
        print("Warning: {0} language not in known languages, defaulting to 'EN'", lang)
        language = 'EN'

    anagrams_map = {}

    for word in words:
        key = 1
        for letter in word:
            key = key * letter_map[language][letter.lower()]

        if  key not in anagrams_map:
            anagrams_map[key] = []

        anagrams_map[key].append(word)

    results = [(k, anagrams_map[k]) for k in anagrams_map if len(anagrams_map[k]) > 1]
    return results
    
def FindAnagrams3(words):
    anagrams_map = {}

    for word in words:
        key = 0
        for letter in word:
            key = key + ord(letter)

        if  key not in anagrams_map:
            anagrams_map[key] = []

        anagrams_map[key].append(word)
        if word == "AD" or word == "BC":
            print("Word '{0}' --> {1}", word, key)

    results = [(k, anagrams_map[k]) for k in anagrams_map if len(anagrams_map[k]) > 1]
    return results
    
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        words_filename = sys.argv[1]
        if os.path.isfile(words_filename):
            with open(words_filename) as infile:
                words = infile.readlines()

            words = [w.strip() for w in words]

    print(FindAnagrams1(words))
    print(FindAnagrams2(words, 'foo'))
    print(FindAnagrams3(words))
