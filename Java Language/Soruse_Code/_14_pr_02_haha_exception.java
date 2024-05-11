public class _14_pr_02_haha_exception {
    public static int Method(int a,int b){
        if (b==0) {
            throw new IllegalArgumentException("Hehe");
        }
        return a/b;
    }
    public static void main(String[] args) {
        try {
            int C=0/0;
            int result = Method(10,0);
            
        } catch (ArithmeticException Error) {
            System.out.printf("Haha");
        } catch (IllegalArgumentException Error){
            System.out.printf("Hehe");

        }
        
            

    }
}
