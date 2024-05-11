import java.util.Scanner;

public class _01_pr_05_integer_input_check {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter A Integer Number-");
        boolean user = input.hasNextInt();

        input.close();
        
        System.out.println("Previous Input was integer-"+ user);
    }
}
