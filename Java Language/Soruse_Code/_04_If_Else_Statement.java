import java.util.Scanner;

public class _04_If_Else_Statement {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num =55;

        System.out.print("Enter A Number that is bigger than num\n");
        int user = input.nextInt();
        input.close();

        if(user>num){
            System.out.print("User Entered Higher Number");            
        }
        else if(user==6){
            System.out.print("User Entered Higher Number");            
        }
        else{
            System.out.print("User Entered Lower Number");
        }
        
    }
    
}