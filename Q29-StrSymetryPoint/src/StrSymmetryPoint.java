// Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
// https://app.codility.com/programmers/trainings/4/str_symmetry_point/
// Write a function:

// class Solution { public int solution(String S); }
// that, given a string S, returns the index (counting from 0) of a character such that the part of the string to the left of that character is a reversal of the part of the string to its right. The function should return −1 if no such index exists.

// Note: reversing an empty string (i.e. a string whose length is zero) gives an empty string.

// For example, given a string:

// "racecar"

// the function should return 3, because the substring to the left of the character "e" at index 3 is "rac", and the one to the right is "car".

// Given a string:

// "x"

// the function should return 0, because both substrings are empty.

// Write an efficient algorithm for the following assumptions:

// - the length of string S is within the range [0..2,000,000].

public class StrSymmetryPoint {
    public static int FindLongestSymmetryPoint(String s) {
        if (s == null || s.length() == 0) {
            return -1;
        }

        if (s.length() == 1) {
            return 0;
        }

        int leftEdge;
        int midpoint = s.length() / 2;
        for (int symmetryPoint = midpoint; symmetryPoint > 0; symmetryPoint--) {
            for (leftEdge = symmetryPoint; leftEdge > 0; leftEdge--) {
                if (symmetryPoint + leftEdge >= s.length()
                        || s.charAt(symmetryPoint - leftEdge) != s.charAt(symmetryPoint + leftEdge)) {
                    break;
                }
            }

            if (leftEdge == 0) {
                return symmetryPoint;
            }
        }

        return -1;
    }

    public static int HasSymmetryPoint(String s) {
        if (s == null || s.length() == 0 || (s.length() & 1) == 0) {
            return -1;
        }

        if (s.length() == 1) {
            return 0;
        }

        int midpoint = s.length() / 2;
        int delta = -1;
        for (delta = midpoint; delta > 0; delta--) {
            if (s.charAt(midpoint - delta) != s.charAt(midpoint + delta)) {
                break;
            }
        }

        if (delta == 0) {
            return midpoint;
        }

        return -1;
    }

}
