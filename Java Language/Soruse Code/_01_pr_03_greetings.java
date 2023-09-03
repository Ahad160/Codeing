import java.util.Scanner;

public class _01_pr_03_greetings {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter Youer Name-");
        String name = input.nextLine();

        input.close();

        System.out.print("Hello " + name + " Have a good day");
    }
}
