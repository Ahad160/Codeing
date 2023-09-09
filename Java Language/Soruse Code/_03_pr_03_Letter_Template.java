import java.util.Scanner;

public class _03_pr_03_Letter_Template {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String letter ="Dear <|Name|>, Thanks a lot";

        System.out.print("Enter Youer Name-");
        String user = input.nextLine();

        input.close();

        System.out.println(letter.replace("<|Name|>",user));

    }
}
 