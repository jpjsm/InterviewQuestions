import java.util.Map;
import java.util.HashMap;

public class FirstUniqueNumber {
    public static int FindFirstUniqueNumber(int[] numbers) {
        Map<Integer, Integer> occurrences = new HashMap<>();

        for (int i = 0; i < numbers.length; i++) {
            if (!occurrences.containsKey(numbers[i])) {
                occurrences.put(numbers[i], 0);
            }

            occurrences.put(numbers[i], occurrences.get(numbers[i]) + 1);
        }

        for (int i = 0; i < numbers.length; i++) {
            if (occurrences.get(numbers[i]) == 1) {
                return numbers[i];
            }
        }

        return -1;
    }
}
