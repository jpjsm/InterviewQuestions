
// Imports
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Random;
import java.util.Set;
import java.util.TreeSet;
// To print debugging messages
// System.out.println("debug message")

public class SmallestIntegerMissingInList {
    public static int smallestIntegerMissingInList1(int[] numbers) {
        Set<Integer> candidates = new HashSet<>();

        for (int candidate : numbers) {
            if (candidate > 0) {
                candidates.add(candidate);
            }
        }

        int missing = 1;
        while (candidates.contains(missing)) {
            missing++;
        }

        return missing;
    }

    public static int smallestIntegerMissingInList2(int[] numbers) {
        Set<Integer> candidates = new TreeSet<>();

        for (int candidate : numbers) {
            if (candidate > 0) {
                candidates.add(candidate);
            }
        }

        int missing = 1;
        for (int candidate : candidates) {
            if (candidate != missing) {
                break;
            }

            missing++;
        }

        return missing;
    }

    public static void main(String[] args) {
        Random random = new Random();
        int arraySize = 10_000_000;
        double fromNanoToMilli = 1.0 / 1_000_000.0;
        int cases = 25;
        for (int i = 0; i < cases; i++) {
            int[] data = new int[arraySize];
            int expectedMissingNumber = -1;

            if (i == 0) {
                for (int j = 0; j < arraySize; j++) {
                    data[j] = 0;
                }
                expectedMissingNumber = 1;
            }

            if (i == 1) {
                for (int j = 0; j < arraySize; j++) {
                    data[j] = j + 1;
                }
                expectedMissingNumber = arraySize + 1;
            }

            if (i > 1) {
                int lowerBound = -random.nextInt(arraySize);
                for (int j = 0; j < arraySize; j++) {
                    data[j] = lowerBound + j;
                }

                int missingIndex = random.nextInt(arraySize);
                expectedMissingNumber = data[arraySize - 1] + 1;
                if (data[missingIndex] > 0) {
                    expectedMissingNumber = data[missingIndex];
                    data[missingIndex] = -data[missingIndex];
                }
            }

            long startTime1 = System.nanoTime();
            int missingNumber1 = smallestIntegerMissingInList1(data);
            long elapsedTimeNanoSeconds1 = System.nanoTime() - startTime1;
            double elapsedTimeMilliSeconds1 = elapsedTimeNanoSeconds1 * fromNanoToMilli;

            long startTime2 = System.nanoTime();
            int missingNumber2 = smallestIntegerMissingInList2(data);
            long elapsedTimeNanoSeconds2 = System.nanoTime() - startTime2;
            double elapsedTimeMilliSeconds2 = elapsedTimeNanoSeconds2 * fromNanoToMilli;

            System.out.println(String.format("Case %1$4d:", i));

            System.out.println(String.format(
                    "- smallestIntegerMissingInList1: expectedMissingNumber = %1$,16d %2$s %3$,16d = missingNumber | Total elapsed execution time: %4$f",
                    expectedMissingNumber, expectedMissingNumber == missingNumber1 ? "==" : "!=", missingNumber1,
                    elapsedTimeMilliSeconds1));
            System.out.println(String.format(
                    "- smallestIntegerMissingInList2: expectedMissingNumber = %1$,16d %2$s %3$,16d = missingNumber | Total elapsed execution time: %4$f",
                    expectedMissingNumber, expectedMissingNumber == missingNumber2 ? "==" : "!=", missingNumber2,
                    elapsedTimeMilliSeconds2));

        }
    }
}
