public class _07_pr_05_Fibonacci_Series {
    static int Fibonacci(int x){
        if (x == 1) {
            return 0;
        } else if (x == 2) {
            return 1;
        } else {
            return Fibonacci(x - 1) + Fibonacci(x - 2);
        }
    }
    
    public static void main(String[] args) {
        int Natural_Number = Fibonacci(8);

        System.out.println(Natural_Number);
    }
}
