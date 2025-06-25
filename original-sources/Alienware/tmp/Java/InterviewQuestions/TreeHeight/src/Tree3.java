// import java.util.regex.*;

public class Tree3 {
    public int Value;
    public Tree3 Left;
    public Tree3 Right;

    public Tree3() {
        Value = 0;
        Left = null;
        Right = null;
    }

    public Tree3(int v, Tree3 l, Tree3 r) {
        Value = v;
        Left = l;
        Right = r;
    }

    public Tree3(String tree) {
        tree = tree.replaceAll("\\s", "").toLowerCase();

        if (tree == null || tree.length() == 0) {
            Value = 0;
            Left = null;
            Right = null;
            return;
        }

        if ((tree.charAt(0) != '(') || (tree.charAt(tree.length() - 1) != ')')) {
            throw new Error(String.format(
                    "ERROR: String representation of Tree3 is invalid. Missing opening or closing parenthesis: ",
                    tree));
        }

        // remove left and right parenthesis
        tree = tree.substring(1, tree.length() - 1);

        //
        // Get value
        //
        int commaIndex = tree.indexOf(",");
        String value_str = tree.substring(0, commaIndex);
        Value = Integer.parseInt(value_str);

        //
        // get left expression: none | (...)
        //
        String lr = tree.substring(commaIndex + 1);
        if (lr.startsWith("none,")) {
            Left = null;
            lr = lr.substring("none,".length());
        } else if (lr.startsWith("(")) {
            int open = 1;
            int close = 0;
            int i = 1;
            while (open > close && i < lr.length()) {
                switch (lr.charAt(i)) {
                    case '(':
                        open++;
                        break;
                    case ')':
                        close++;
                        break;
                    default:
                        break;
                }
                i++;
            }

            if (open > close) {
                throw new Error("Left node: Unbalanced parenthesis expression: " + lr);
            }

            String left_node = lr.substring(0, i);
            lr = lr.substring(i + 1);
            Left = new Tree3(left_node);
        } else {
            throw new Error("Left node invalid initial character: " + lr);
        }

        //
        // get right expression: none | (...)
        //
        if (lr.equalsIgnoreCase("none")) {
            Right = null;
        } else if (lr.startsWith("(")) {
            int open = 1;
            int close = 0;
            int i = 1;
            while (open > close && i < lr.length()) {
                switch (lr.charAt(i)) {
                    case '(':
                        open++;
                        break;
                    case ')':
                        close++;
                        break;
                    default:
                        break;
                }
                i++;
            }

            if (open > close) {
                throw new Error("Right node: Unbalanced parenthesis expression: " + lr);
            }

            String right_node = lr.substring(0, i);
            Right = new Tree3(right_node);
        } else {
            throw new Error("Right node invalid initial character: " + lr);
        }
    }

    public static int TreeHeight(Tree3 T) {
        return GetTreeDepth(T);
    }

    private static int GetTreeDepth(Tree3 T) {
        if (T == null) {
            return 0;
        }

        int left = 0;
        int right = 0;

        if (T.Left != null) {
            left = GetTreeDepth(T.Left) + 1;
        }

        if (T.Right != null) {
            right = GetTreeDepth(T.Right) + 1;
        }

        return left > right ? left : right;
    }

}
