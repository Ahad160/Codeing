import java.util.Scanner;

public class _07_pr_01_Fuction_Multiplication {

    static void Multitable(int user){
        for(int i=1;i<=10;i++){
            System.out.printf("%dX%d=%d\n",user,i,user*i);
        }
       
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a Num of Table-");
        int user = input.nextInt();
        input.close();

        Multitable(user);
    }    
}