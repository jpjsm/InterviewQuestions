import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Replace2 {
    public static String rFirst(String original, String replacementPattern, String replacementValue) {
        Pattern pattern = Pattern.compile(replacementPattern);
        Matcher matcher = pattern.matcher(original);
        StringBuilder sb = new StringBuilder();
        if (matcher.find()) {
            matcher.appendReplacement(sb, replacementValue);
        }
        matcher.appendTail(sb);
        return sb.toString();
    }

    public static String rAll(String original, String replacementPattern, String replacementValue) {
        Pattern pattern = Pattern.compile(replacementPattern);
        Matcher matcher = pattern.matcher(original);
        StringBuilder sb = new StringBuilder();
        while (matcher.find()) {
            matcher.appendReplacement(sb, replacementValue);
        }
        matcher.appendTail(sb);
        return sb.toString();
    }
}
