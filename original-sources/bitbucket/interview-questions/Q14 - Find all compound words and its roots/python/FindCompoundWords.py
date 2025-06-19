#!/usr/bin/env python3
import sys
import os.path

words =[
    "a",
    "air",
    "airplane",
    "and",
    "angel",
    "away",
    "ball",
    "big",
    "blue",
    "boa",
    "board",
    "boardwalk",
    "body",
    "bodyguard",
    "can",
    "cart",
    "cartwheel",
    "check",
    "come",
    "dead",
    "deadend",
    "dog",
    "doghouse",
    "down",
    "end",
    "find",
    "for",
    "funny",
    "go",
    "guard",
    "help",
    "here",
    "horse",
    "horseplay",
    "house",
    "i",
    "in",
    "is",
    "it",
    "jump",
    "little",
    "look",
    "mail",
    "mailman",
    "make",
    "man",
    "me",
    "mid",
    "midnight",
    "moon",
    "moonrock",
    "my",
    "night",
    "not",
    "one",
    "out",
    "pay",
    "paycheck",
    "plane",
    "play",
    "racquet",
    "racquetball",
    "red",
    "rock",
    "run",
    "said",
    "see",
    "skate",
    "skateboard",
    "take",
    "takedown",
    "takeout",
    "the",
    "three",
    "to",
    "two",
    "up",
    "walk",
    "we",
    "wheel",
    "where",
    "yellow",
    "you"
]

def FindCompoundWords(words):
    word_dict = {}
    for word in words:
        word_dict[word] = []

    for keyword in word_dict:
        for i in range(1,len(keyword)):
            left = keyword[0:i]
            right = keyword[i:]
            if (left in word_dict) and (right in word_dict):
                word_dict[keyword].append((left, right))

    results = [(k, word_dict[k]) for k in word_dict if len(word_dict[k]) > 0]
    return results



if __name__ == "__main__":
    if len(sys.argv) > 1:
        words_filename = sys.argv[1]
        if os.path.isfile(words_filename):
            with open(words_filename) as infile:
                words = infile.readlines()

            words = [w.strip() for w in words]

    print(FindCompoundWords(words))
