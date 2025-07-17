import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class GenerateBalancedParenthesis {
    private static Map<Integer, List<String>> generatedBalancedParenthesis = new HashMap<>();

    public static List<String> GenerateBalancedParentheses(int n) {
        if (n < 0) {
            throw new Error(String.format("n = %1$d must be greator or equal to Zero."));
        }

        if (generatedBalancedParenthesis.containsKey(n)) {
            return generatedBalancedParenthesis.get(n);
        }

        List<String> results = new ArrayList<>();
        if (n == 0) {
            results.add("");
            generatedBalancedParenthesis.put(n, results);
            return results;
        }

        for (int i = 0; i < n; i++) {
            for (String l : GenerateBalancedParentheses(i)) {
                for (String r : GenerateBalancedParentheses((n - 1) - i)) {
                    results.add(String.format("(%s)%s", l, r));
                }
            }
        }

        generatedBalancedParenthesis.put(n, results);
        return results;
    }

    public static void main(String[] args) {
        for (int i = 0; i < 7; i++) {
            System.out.println(GenerateBalancedParentheses(i));
        }
    }
}
