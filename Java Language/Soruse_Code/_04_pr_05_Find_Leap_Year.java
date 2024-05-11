import java.util.Scanner;

public class _04_pr_05_Find_Leap_Year {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter Any Year-");
        int year = input.nextInt();

        input.close();

        if(year%4==0 && year%100!=0 || year%400==0){
            System.out.printf("%d is Leap Year",year);
        }
        else{
            System.out.printf("%d is Not Leap Year",year);

        }

        
    }
    
}