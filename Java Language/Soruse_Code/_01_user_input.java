import java.util.Scanner;

public class _01_user_input {
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);

        System.out.println("Enter the 1st Number");
        int a =input.nextInt();

        System.out.println("Enter the 2nd Number");
        int b =input.nextInt();

        System.out.println("Enter Youer Name");
        String name = input.next();


        input.close(); //Maybe It Opsonal

        int sum=a+b;

        System.out.println("The Sum of A and B is:" + sum);
        System.out.println(name);





        
    }
}
