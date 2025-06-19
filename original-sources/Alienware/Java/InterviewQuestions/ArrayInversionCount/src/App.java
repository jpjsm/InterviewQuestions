import java.util.Collections;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.Comparator;

public class App {
    public static void main(String[] args) {
        int top = 44722;
        int[] longArray = new int[top];
        for (int i = 0; i < top; i++) {
            longArray[i] = top - i;
        }

        List<TestCase> testCases = new ArrayList<>();
        testCases.add(new TestCase(longArray, -1));
        testCases.add(new TestCase(new int[] { 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 }, 45));
        testCases.add(new TestCase(new int[] { 2, 1, 2, 1, 2, 1, 2, 1 }, 10));
        testCases.add(new TestCase(new int[] { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 }, 0));
        testCases.add(new TestCase(new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9 }, 0));
        testCases.add(new TestCase(new int[] { -1, 6, 3, 4, 7, 4 }, 4));

        testCases.sort((a, b) -> Integer.compare(a.Expected, b.Expected));
        testCases.sort(Comparator.comparingInt(TestCase::getExpected));

        Collections.sort(testCases, (a, b) -> Integer.compare(a.Expected, b.Expected));
        Collections.sort(testCases, Comparator.comparingInt(TestCase::getExpected));

        ArrayInversionCount sol = new ArrayInversionCount();

        for (TestCase testCase : testCases) {
            int actual = sol.solution(testCase.Test);

            String msg = String.format("Success ! actual %d == %d expected.", actual, testCase.Expected);
            if (actual != testCase.Expected) {
                msg = String.format("FAILURE ! actual %d != %d expected.", actual, testCase.Expected);
            }
            System.out.println(msg);
        }
    }
}
