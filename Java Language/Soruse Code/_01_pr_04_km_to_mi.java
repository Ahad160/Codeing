import java.util.Scanner;

public class _01_pr_04_km_to_mi {
    public static void main(String[] args) {
        float mi = 1.609344F ;

        Scanner input = new Scanner(System.in);

        System.out.println("Kilometer To Miles Converter");
        System.out.print("Enter Kilometer-");
        float Kilometer = input.nextFloat();

        input.close();
        
        float Converter = Kilometer/mi;

        System.out.println(Kilometer+" kilometer To Miles "+ Converter);




    }   
}
