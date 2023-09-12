import java.util.Scanner;

public class _04_pr_03_Income_Tax {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter Youer Income in Lack-");
        float Income = input.nextFloat();
        input.close();
        if(Income>2.5 && Income<5.0){
            System.out.println("Youer Income Tax in 5%");
        }
        else if(Income>5.0 && Income<10.0){
            System.out.println("Youer Income Tax in 20%");

        }
        else if(Income>10.0){
            System.out.println("Youer Income Tax in 30%");
            
        }
        else
        {
            System.out.println("You Dont Have to Give Tax");
        }

        
    }
}
