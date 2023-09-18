import java.util.Scanner;

public class _06_pr_02_find_int_Array {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int Array[] = {50,56,90,66};
        boolean check=false;

        System.out.printf("Enter A Number-");
        input.close();
        int user = input.nextInt();

        for(int element:Array){
            if(user==element){
                check=true;
                break;
            }
        }

        if(check==true){
            System.out.printf("The Entered Number is Present in Array");
        }
        else{
            System.out.printf("The Entered Number is Not Present in Array");

        }

    }

 }
