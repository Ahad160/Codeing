import java.util.Scanner;

public class _05_pr_06_Sum_Multi_Table {
    public static void main(String[] args) {
        int sum=0;
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter a Num of Table-");
        int user = input.nextInt();
        input.close();


        for(int i=1;i<=10;i++){
            
            System.out.printf("%dX%d=%d\n",user,i,user*i);
            sum+=user*(i+1);
            
        }
        System.out.printf("Sum of %d is %d",user,sum);
    }
}