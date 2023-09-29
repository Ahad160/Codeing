import java.util.Random;
import java.util.Scanner;

class Guess{
    Scanner input = new Scanner(System.in);
    int A=0; //For Times of Guess

    
    public Guess(int Gen){
        
        System.out.printf("Enter A Number(0-100)---");

        while (true) {

            int user = input.nextInt();

            if (user==Gen) {
                System.out.printf("You Guess The Right Number 😃😃 In %d Terms\n",A);
                break;
            }
            else if (user>=Gen) {
                System.out.printf("Please Guess Lower Number-");
                A+=1;
                continue;
            }
            else if (user<=Gen) {
                System.out.printf("Please Guess Higher Number-");
                A+=1;
                continue;

            }
        }
    }
    public void PPP(){

    }

}



public class _09_Ex_Guess_The_Number {
    public static void main(String[] args) {
        Random random = new Random();
                int Gen = random.nextInt(100);
        System.out.printf("%d\n",Gen);

        Guess object = new Guess(Gen);

        object.PPP();
        
    }    
}
