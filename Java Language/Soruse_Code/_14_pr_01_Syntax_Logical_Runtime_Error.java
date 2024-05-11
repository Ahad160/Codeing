public class _14_pr_01_Syntax_Logical_Runtime_Error {
    public static void main(String[] args) {
        //Syntax Error
        // int = 0;

        //logical Error
        int a = 5;
        if (a==0) {
            System.out.printf("A is 0");
        }
        // Runtime Error
        int C=0/0;
        System.out.println(C);


    }
}
