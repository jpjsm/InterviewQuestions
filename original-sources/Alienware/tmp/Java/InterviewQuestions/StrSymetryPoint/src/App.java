public class App {
    public static void main(String[] args) {
        String[] words = {
                "naan",
                "abcdefghijihgfedcba",
                "anabana",
                "x",
                "ana",
        };

        String msg = "";
        for (String word : words) {
            int symmetryPoint = StrSymmetryPoint.HasSymmetryPoint(word);

            switch (symmetryPoint) {
                case -1:
                    msg = "No symmetry found: " + word;
                    break;
                case 0:
                    msg = "Singleton string: " + word;
                    break;

                default:
                    msg = String.format("Symmetry at char %d --> '%s': %s <= %s", symmetryPoint,
                            word.charAt(symmetryPoint),
                            word.substring(0, 2 * symmetryPoint + 1), word);
                    break;
            }

            System.out.println(msg);
        }
    }

}