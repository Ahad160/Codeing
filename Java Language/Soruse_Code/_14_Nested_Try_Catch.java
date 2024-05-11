import java.util.InputMismatchException;
import java.util.Scanner;

public class _14_Nested_Try_Catch {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        try {
            System.out.printf("Enter 1st Code:-");
            int user = input.nextInt();
            System.out.printf("Enter 2nd Code:-");
            int user2 = input.nextInt();
            try {
                int Divide = user/user2;
                System.out.printf("%d", Divide);

            } catch (ArithmeticException Error) {
                System.out.printf("Divide in Failedn\n");
            }


            System.out.printf("%d",user);
            System.out.printf("%d",user2);
            
        input.close();    


            
        } catch (InputMismatchException Error) {
            System.out.printf("Enter Number Only");
        }

    }
}
