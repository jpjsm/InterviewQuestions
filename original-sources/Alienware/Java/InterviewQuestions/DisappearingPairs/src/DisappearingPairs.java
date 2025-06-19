import java.util.List;
import java.util.ArrayList;

public class DisappearingPairs {
    public static String RemovePairs(String s) {
        List<Character> results = new ArrayList<>(s.length());

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (results.isEmpty()) {
                results.add(c);
                continue;
            }

            if (c == results.getLast()) {
                results.removeLast();
                continue;
            }

            results.add(c);
        }

        return CharListToString(results);
    }

    public static String CharListToString(List<Character> l) {
        StringBuilder sb = new StringBuilder(l.size());
        for (char c : l) {
            sb.append(c);
        }

        return sb.toString();
    }

}
