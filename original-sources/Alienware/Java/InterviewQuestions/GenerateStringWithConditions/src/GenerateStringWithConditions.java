public class GenerateStringWithConditions {
    public static String GenerateABsWithoutTripleRepetition(int A, int B) {
        String a = "a";
        String b = "b";
        boolean switched = Boolean.FALSE;

        if (B > A) {
            int itmp = B;
            B = A;
            A = itmp;

            String stmp = b;
            b = a;
            a = stmp;

            switched = Boolean.TRUE;
        }

        String result = "";

        int delta = A - B;
        if (delta <= 2) {
            for (int i = 0; i < B; i++) {
                result += a + b;
            }

            result = switch (delta) {
                case 0 -> result;
                case 1 -> result + a;
                case 2 -> a + result + a;
                default -> throw new Error(String.format(
                        "Un-expected delta value! Allowed values are zero, one, or two. Values received: A=%d, B=%d, C=%d",
                        A, B, delta));
            };
            return result;
        }

        if (B == 0) {
            return a.repeat(A);
        }

        int newA = A - 2;
        int newB = B - 1;

        return (a + a + b) + GenerateABsWithoutTripleRepetition(switched ? newB : newA, switched ? newA : newB);
    }
}
