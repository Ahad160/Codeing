import java.util.Scanner;

public class _04_pr_06_Website_Type {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter A Website--");
        String website = input.nextLine();

        input.close();


        if(website.endsWith(".com")){
            System.out.printf("%s is a Commercial Website",website);
        }
        else if(website.endsWith(".org")){
            System.out.printf("%s is a organigation Website",website);
        }
        else if(website.endsWith(".in")){
            System.out.printf("%s is a indian Website",website);
        }
        else{
            System.out.printf("%s is a Unknown Website",website);
        }
        

    }
}
