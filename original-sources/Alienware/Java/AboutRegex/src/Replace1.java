public class Replace1 {
    public static String rFirst(String original, String replacementPattern, String replacementValue) {
        String r = original.replaceFirst(replacementPattern, replacementValue);
        return r;
    }

    public static String rAll(String original, String replacementPattern, String replacementValue) {
        String r = original.replaceAll(replacementPattern, replacementValue);
        return r;
    }
}
