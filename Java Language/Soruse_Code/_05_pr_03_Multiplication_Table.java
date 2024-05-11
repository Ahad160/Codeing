import java.util.Scanner;

public class _05_pr_03_Multiplication_Table {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter a Num of Table-");
        int user = input.nextInt();
        input.close();


        for(int i=1;i<=10;i++){
            System.out.printf("%dX%d=%d\n",user,i,user*i);
        }
    }
}
