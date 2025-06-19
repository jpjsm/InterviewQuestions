public class App {
    public static void main(String[] args) {
        String[] testCases = {
                "==> MURCIELAGO, EUFORIA, RIACHUELO, COMUNICARSE|A|a",
                "==> MURCIELAGO, EUFORIA, RIACHUELO, COMUNICARSE|E|e",
                "==> MURCIELAGO, EUFORIA, RIACHUELO, COMUNICARSE|I|i",
                "==> MURCIELAGO, EUFORIA, RIACHUELO, COMUNICARSE|O|o",
                "==> MURCIELAGO, EUFORIA, RIACHUELO, COMUNICARSE|U|u"
        };

        for (String testCase : testCases) {
            String[] items = testCase.split("\\|");
            System.out.println(Replace1.rFirst(items[0], items[1], items[2]));
            System.out.println(Replace2.rFirst(items[0], items[1], items[2]));
        }

        System.out.println("\n=======================================================\n");

        for (String testCase : testCases) {
            String[] items = testCase.split("\\|");
            System.out.println(Replace1.rAll(items[0], items[1], items[2]));
            System.out.println(Replace2.rAll(items[0], items[1], items[2]));
        }

        System.out.println("\n=======================================================\n");
    }
}
