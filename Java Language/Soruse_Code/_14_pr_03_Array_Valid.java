import java.util.Scanner;

public class _14_pr_03_Array_Valid {
    public static void main(String[] args) {
        boolean flag = true;
        int [] mark = new int[3];
        mark[0]=7;
        mark[1]=70;
        mark[2]=9;
        Scanner input = new Scanner(System.in);
        int index;
        int i=0;
        while (flag && i <5) {
            try {
                System.out.printf("Enter the index-");
                index = input.nextInt();
                System.out.printf("The value of mark[index]" + mark[index]);
                break;
            } catch (Exception e) {
                System.out.printf("Invalid Index");
                i++;
            }
        }


        }
    }

