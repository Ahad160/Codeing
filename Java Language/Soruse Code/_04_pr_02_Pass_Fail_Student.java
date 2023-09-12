import java.util.Scanner;

public class _04_pr_02_Pass_Fail_Student {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter 1st Subject Mark-");
        int mk1 = input.nextInt();

        System.out.print("Enter 2nd Subject Mark-");
        int mk2 = input.nextInt();

        System.out.print("Enter 3rd Subject Mark-");
        int mk3 = input.nextInt();

        float avg = (mk1+mk2+mk3)/3.0f;

        input.close();

        if(avg>=40 && mk1>=33 && mk2>=33 && mk3>=33){
            System.out.println("You Pass");
        }
        else{
            System.out.println("You Fail");

        }

    



        
    }
}
