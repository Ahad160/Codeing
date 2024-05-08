public class _14_Try_Catch {
    public static void main(String[] args) {
        int A=1;
        int B=0;
        
        try {
            int C= A/B;
            System.out.printf("%d",C);
        } catch (Exception Error) {
            System.out.printf("Divide By Zero Error");
        }
        

        
    }
}
