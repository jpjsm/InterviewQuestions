public class TestCase {
    public int Expected;
    public int[] Test;

    public TestCase(int[] t, int e) {
        Test = t;
        Expected = e;
    }

    public int getExpected() {
        return Expected;
    }
}
