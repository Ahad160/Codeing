import java.util.Scanner;

public class _01_pr_01_sum_numbers {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter 1st Number-");
        int val_1 = input.nextInt();
        
        System.out.print("Enter 2nd Number-");
        int val_2 = input.nextInt();

        System.out.print("Enter 3rd Number-");
        int val_3 = input.nextInt();

        input.close();
        
        int sum = val_1+val_2+val_3;

        System.out.println("The Sum of Three Number is-"+sum);
    }
}
