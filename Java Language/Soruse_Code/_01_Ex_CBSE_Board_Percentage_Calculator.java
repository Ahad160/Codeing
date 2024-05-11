import java.util.Scanner;

public class _01_Ex_CBSE_Board_Percentage_Calculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.println("CBSE_Board_Percentage_Calculator");

        System.out.print("Enter Subject-1 Mark-");
        float Subject1 = input.nextInt();
            
        System.out.print("Enter Subject-2 Mark-");
        float Subject2 = input.nextInt();

        System.out.print("Enter Subject-3 Mark-");
        float Subject3 = input.nextInt();

        System.out.print("Enter Subject-4 Mark-");
        float Subject4 = input.nextInt();

        System.out.print("Enter Subject-5 Mark-");
        float Subject5 = input.nextInt();

        input.close();

        float Total =Subject1+Subject2+Subject3+Subject4+Subject5;
        float formula = (Total/500)*100;

        System.out.println("Youer Percentage is -" + formula);


    }
}
