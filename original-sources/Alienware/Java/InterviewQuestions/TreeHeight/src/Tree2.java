import java.util.regex.*;

public class Tree2 {
    private static String valueRegex = "\\s*([0-9]+)\\s*";
    private static String nodeRegex = "\\s*(none|\\(.+?\\))\\s*";
    private static String commaRegex = "\\s*,\\s*";
    private static Pattern TreePattern = Pattern
            .compile("(?i)^\\s*\\(" + valueRegex + commaRegex + nodeRegex + commaRegex + nodeRegex + "\\)\\s*$");

    public int Value;
    public Tree2 Left;
    public Tree2 Right;

    public Tree2() {
        Value = 0;
        Left = null;
        Right = null;
    }

    public Tree2(int v, Tree2 l, Tree2 r) {
        Value = v;
        Left = l;
        Right = r;
    }

    public Tree2(String tree) {
        tree = tree.trim();
        if (tree == null || tree.length() == 0) {
            Value = 0;
            Left = null;
            Right = null;
            return;
        }

        Matcher treeMatcher = TreePattern.matcher(tree);
        if (!treeMatcher.find()) {
            throw new Error("Not a tree pattern! value received: " + tree);
        }

        Value = Integer.parseInt(treeMatcher.group(1));
        String strLeftTree = treeMatcher.group(2);
        Left = strLeftTree.equalsIgnoreCase("none") ? null : new Tree2(strLeftTree);
        String strRightTree = treeMatcher.group(3);
        Right = strRightTree.equalsIgnoreCase("none") ? null : new Tree2(strRightTree);
    }

    public static int TreeHeight(Tree2 T) {
        return GetTreeDepth(T);
    }

    private static int GetTreeDepth(Tree2 T) {
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
