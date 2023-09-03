import java.util.Scanner;

public class _01_pr_02_CGPA_calulator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter 1st Subject Number-");
        float Subject_1 = input.nextInt();
        
        System.out.print("Enter 2nd Subject Number-");
        float Subject_2 = input.nextInt();

        System.out.print("Enter 3rd Subject Number-");
        float Subject_3 = input.nextInt();

        input.close();
        
        float CGPA=(Subject_1+Subject_2+Subject_3)/30;

        System.out.println(CGPA);


        
       
    }
}
