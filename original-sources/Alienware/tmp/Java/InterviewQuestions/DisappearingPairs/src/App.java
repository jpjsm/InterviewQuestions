public class App {
    public static void main(String[] args) {
        String[] testCases = {
                "ACCAABBC",
                "ABCBBCBA",
                "AABBCCBAABCCCBBBBC"
        };

        for (String test : testCases) {
            System.out.println(test + " --> »" + DisappearingPairs.RemovePairs(test) + "«");
        }
    }
}
