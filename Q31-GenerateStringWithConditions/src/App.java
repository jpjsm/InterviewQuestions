import java.io.FileWriter;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.File;
import java.util.List;
import java.util.ArrayList;

public class App {
    public static String TestCasesPath = "C:\\tmp\\Java\\GenerateStringWithConditions\\src\\TestCases.txt";

    public static void main(String[] args) {
        int[][] testValues = { {} };
        String[] expectedResults = { "" };

        File testCases = new File(App.TestCasesPath);
        if (testCases.exists()) {
            List<int[]> generated_arguments = new ArrayList<int[]>();
            List<String> generated_results = new ArrayList<>();
            try (BufferedReader reader = new BufferedReader(new FileReader(TestCasesPath))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    String[] line_values = line.split("\t");
                    int a = Integer.parseInt(line_values[0]);
                    int b = Integer.parseInt(line_values[1]);
                    String expected = line_values.length == 3 ? line_values[2] : "";
                    int[] pair = { a, b };
                    generated_arguments.add(pair);
                    generated_results.add(expected);
                }

                testValues = generated_arguments.toArray(new int[generated_arguments.size()][]);
                expectedResults = generated_results.toArray(new String[0]);
            } catch (IOException e) {
                e.printStackTrace();
            }

        } else {
            testValues = new int[][] {
                    { 0, 0 },
                    { 1, 1 },
                    { 2, 2 },
                    { 1, 0 },
                    { 0, 1 },
                    { 2, 0 },
                    { 0, 2 },
                    { 1, 3 },
                    { 3, 1 },
                    { 5, 2 },
                    { 2, 5 },
                    { 6, 2 },
                    { 2, 6 },
                    { 7, 2 },
                    { 2, 7 },

            };

            expectedResults = new String[] {
                    "",
                    "ab",
                    "abab",
                    "a",
                    "b",
                    "aa",
                    "bb",
                    "bbab",
                    "aaba",
                    "aabaaba",
                    "bbabbab",
                    "aabaabaa",
                    "bbabbabb",
                    "aabaabaaa",
                    "bbabbabbb",

            };
        }

        for (int i = 0; i < testValues.length; i++) {
            int A = testValues[i][0];
            int B = testValues[i][1];

            String expected = expectedResults[i];

            String actual = GenerateStringWithConditions.GenerateABsWithoutTripleRepetition(A, B);

            int expectedException = (A > (2 * B + 2)) || (B > (2 * A + 2)) ? 1 : 0;
            int throwsTripleConsecutiveError = actual.contains("aaa") || actual.contains("bbb") ? 2 : 0;
            int throwsMismatchErrorActualVsExpected = !actual.equals(expected) ? 4 : 0;

            int errorBitmap = throwsMismatchErrorActualVsExpected + throwsTripleConsecutiveError + expectedException;

            String msg = switch (errorBitmap) {
                case 0 ->
                    String.format("PERFECT    | (%2d, %2d) | expect Exception %s | actual == expected => %s <--> %s", A,
                            B, expectedException == 1 ? "true" : "false", actual, expected);
                case 1 ->
                    String.format("REVIEW     | (%2d, %2d) | expect Exception %s | actual == expected => %s <--> %s", A,
                            B, expectedException == 1 ? "true" : "false", actual, expected);
                case 2 ->
                    String.format("CRITICAL   | (%2d, %2d) | expect Exception %s | actual == expected => %s <--> %s", A,
                            B, expectedException == 1 ? "true" : "false", actual, expected);
                case 3 ->
                    String.format("OK         | (%2d, %2d) | expect Exception %s | actual == expected => %s <--> %s", A,
                            B, expectedException == 1 ? "true" : "false", actual, expected);
                case 4 ->
                    String.format("TEST ERROR | (%2d, %2d) | expect Exception %s | actual != expected => %s <--> %s", A,
                            B, expectedException == 1 ? "true" : "false", actual, expected);
                case 5 ->
                    String.format("TEST ERROR | (%2d, %2d) | expect Exception %s | actual != expected => %s <--> %s", A,
                            B, expectedException == 1 ? "true" : "false", actual, expected);
                case 6 ->
                    String.format("CRITICAL   | (%2d, %2d) | expect Exception %s | actual != expected => %s <--> %s", A,
                            B, expectedException == 1 ? "true" : "false", actual, expected);
                case 7 ->
                    String.format("CRITICAL   | (%2d, %2d) | expect Exception %s | actual != expected => %s <--> %s", A,
                            B, expectedException == 1 ? "true" : "false", actual, expected);
                default -> throw new Error(String.format(
                        "Un-expected errorBitmap! Allowed values are [0..7]. Values received: errorBitmap=%d, throwsTripleConsecutiveError= %d, throwsMismatchErrorActualVsExpected=%d",
                        errorBitmap, throwsTripleConsecutiveError, throwsMismatchErrorActualVsExpected));
            };

            System.out.println(msg);
        }

        System.out.println("Begin generaring strings.");

        try (FileWriter writer = new FileWriter(TestCasesPath)) {
            for (int a = 0; a <= 100; a++) {
                for (int b = 0; b <= 100; b++) {
                    String actual = GenerateStringWithConditions.GenerateABsWithoutTripleRepetition(a, b);

                    boolean throwsTripleConsecutiveError = actual.contains("aaa") || actual.contains("bbb");
                    if (throwsTripleConsecutiveError) {
                        boolean expectedException = (a > (2 * b + 2)) || (b > (2 * a + 2));
                        if (expectedException) {
                            continue;
                        }

                        int indexOfAAA = actual.indexOf("aaa");
                        int indexOfBBB = actual.indexOf("bbb");

                        int index = indexOfBBB;
                        if (indexOfAAA > 0) {
                            index = indexOfAAA;
                        }
                        System.out.println(String.format("ERROR: (%2d, %2d) First error at: %3d --> %s $s", a, b, index,
                                actual.substring(0, index), actual.substring(index)));
                    }

                    writer.append(String.format("%d\t%d\t%s\n", a, b, actual));

                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("Finished generaring strings.");

    }
}
