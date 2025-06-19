public class Tree {
    public int Value;
    public Tree Left;
    public Tree Right;

    public Tree() {
        Value = 0;
        Left = null;
        Right = null;
    }

    public Tree(int v, Tree l, Tree r) {
        Value = v;
        Left = l;
        Right = r;
    }

    public Tree(String tree) {
        tree = tree.trim();

        if (tree == null || tree.length() == 0) {
            Value = 0;
            Left = null;
            Right = null;
            return;
        }

        if ((tree.charAt(0) != '(') || (tree.charAt(tree.length() - 1) != ')')) {
            throw new Error(String.format(
                    "ERROR: String representation of Tree is invalid. Missing opening or closing parenthesis: ", tree));
        }

        tree = tree.substring(1, tree.length());

        if (tree.indexOf('(') == -1 && tree.indexOf(')') == -1) {
            // leaf node
            String[] parts = tree.split(",");

            if (parts.length != 3) {
                throw new Error(String.format(
                        "ERROR: leaf nodes must be made of three parts! this node has too few or too many parts: %d --> %s",
                        parts.length, tree));
            }
            Value = Integer.parseInt(parts[0]);

            if (!parts[1].trim().equalsIgnoreCase("None")) {
                throw new Error(String.format(
                        "ERROR: leaf left-node string representation must be 'None'. Received value: %s", parts[1]));
            }

            Left = null;

            if (!parts[2].trim().equalsIgnoreCase("None")) {
                throw new Error(String.format(
                        "ERROR: leaf right-node string representation must be 'None'. Received value: %s", parts[2]));
            }

            Right = null;

            return;
        }

        Value = Integer.parseInt(tree.substring(0, tree.indexOf(',')).trim());

        int commaPosition = tree.indexOf(',');
        String lr = tree.substring(commaPosition + 1);
        lr = lr.trim();

        if (lr.substring(0, 4).equalsIgnoreCase("none")) {
            Left = null;
            lr = lr.substring(4);
        } else if (lr.charAt(0) == '(') {
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

            Left = new Tree(lr.substring(0, i));
        } else {
            throw new Error(String.format(
                    "ERROR: A node string representation must begin with an opening parenthesis '('. Received value: %s",
                    lr));
        }

        lr = lr.trim();

        if (lr.charAt(0) != ',') {
            throw new Error(String.format("ERROR: missing field separator for right field. Received value %s", lr));
        }

        lr = lr.substring(1).trim();
        if (lr.substring(0, 4).equalsIgnoreCase("none")) {
            Right = null;
        } else if (lr.charAt(0) == '(') {
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

            Right = new Tree(lr.substring(0, i));
        } else {
            throw new Error(String.format(
                    "ERROR: A node string representation must begin with an opening parenthesis '('. Received value: %s",
                    lr));
        }

    }

    public static int TreeHeight(Tree T) {
        return GetTreeDepth(T);
    }

    private static int GetTreeDepth(Tree T) {
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
