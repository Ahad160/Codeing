public class _14_Throws {

    public static int divide(int a, int b) throws ArithmeticException{
        int Result=a/b;
        return Result;
    }

    public static void main(String[] args) {
        try {
            int c = divide(0, 0);
            System.out.println(c);
        } catch (Exception e) {
            System.out.printf("Exception");
        }
    }
}
