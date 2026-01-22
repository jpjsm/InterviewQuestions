# Justified Formatting

Given a long list of words, write the words in a rectangular array of width '`w`'
characters and '`l`' lines per page. Assume the long list is just one paragraph.

All lines should be of the same length `w`, with no spaces at the end; words
cannot be split. If a word cannot be placed in the line, all words in the line
should be separated by a similar number of spaces. The maximum number of spaces
between two words should not be greater than 1 space to the minimum number of
spaces between words.

- Maximum spaces should be on the right side of the line.
- Last line of the paragraph should be left justified, with single spaces
between words.

Given the following text:

```txt
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.
```

Format the text justified with `w = 64` and `l = 24`.

The generated formatted text should look like this:

```txt
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed  do
eiusmod tempor incididunt ut labore et dolore magna  aliqua.  Ut
enim ad minim veniam, quis nostrud exercitation ullamco  laboris
nisi ut aliquip ex ea commodo consequat.Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum  dolore  eu  fugiat
nulla pariatur. Excepteur sint occaecat cupidatat non  proident,
sunt in culpa qui officia deserunt mollit anim id est laborum.
```
