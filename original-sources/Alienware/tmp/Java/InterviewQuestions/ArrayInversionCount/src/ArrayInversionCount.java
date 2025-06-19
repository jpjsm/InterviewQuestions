import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class ArrayInversionCount {
    public ArrayInversionCount() {

    }

    public int solution(int[] A) {
        List<Integer> sorted = new ArrayList<Integer>();
        for (int n : A) {
            sorted.add(n);
        }

        Collections.sort(sorted);

        int count = 0;
        int i = 0;
        while (!sorted.isEmpty() && i < A.length) {
            int seek = A[i];
            int pos = Collections.binarySearch(sorted, seek);
            if (pos > 0) {
                while (pos > 0 && sorted.get(pos - 1) == seek) {
                    pos--;
                }
                count += pos;
            }

            if (count > 1_000_000_000) {
                return -1;
            }

            sorted.remove(pos);
            i++;
        }

        return count;
    }

}
