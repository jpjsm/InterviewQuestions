
public class TreeHeight {
    class Tree {
        public int x;
        public Tree l;
        public Tree r;
    }

    public int solution(Tree T) {
        return GetTreeDepth(T);
    }

    private int GetTreeDepth(Tree T) {
        if (T == null) {
            return 0;
        }

        int left = 0;
        int right = 0;

        if (T.l != null) {
            left = GetTreeDepth(T.l) + 1;
        }

        if (T.r != null) {
            right = GetTreeDepth(T.r) + 1;
        }

        return left > right ? left : right;
    }
}
