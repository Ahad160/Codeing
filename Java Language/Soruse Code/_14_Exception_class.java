import java.util.Scanner;

/**
 * MyExecption
 */
 class MyExecption extends Exception {

    @Override
    public String toString(){
        return "I am to string()\n";
    }

    @Override
    public String getMessage(){
        return "I am getMessage()\n";
    }
}

public class _14_Exception_class {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int user;
        user= input.nextInt();

        if (user<10) {
            try {
                throw new MyExecption();
                // throw new ArithmeticException("This is a ArithmeticException");
            } catch (Exception e) {
                System.out.printf(e.getMessage());
                System.out.printf(e.toString());
                // e.printStackTrace(); //show error line
 

            }
        }

        
    }
}
