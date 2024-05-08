public class _14_Handling_Specific_Exceptions {
    public static void main(String[] args) {
     
        int A=1;
        int B=0;
        
        try {
            int C= A/B;
            System.out.printf("%d",C);
        } catch (ArithmeticException Error) {
            System.out.printf("Divide By Zero Error");
        } catch(Exception Error){
            System.out.printf("Error is Rised");
        }
        

      
       

    }
}
