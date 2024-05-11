import java.util.Scanner;

public class _02_pr_03_Compare_two_value {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int A=65;
        System.out.println("Enter A Number");
        int user = input.nextInt();

        input.close();

        boolean compare=(user>A);
        System.out.println("Computer Default Value And User Entered Value Same " + compare);
    }
}