import java.util.Scanner;
import java.util.Random;

public class _04_Ex_Rock_Paper_Scissors {
    public static void main(String[] args) {
        Random ran =new Random();
        int Random = ran.nextInt(3);

        Scanner input = new Scanner(System.in);
        System.out.print("Choose Any Off Them\n0 = rock\n1 = paper\n2 = Scissors\n");
        int user = input.nextInt();
        input.close();

        String output =null;

        // 0 = rock
        // 1 = paper
        // 2 = Scissors
        if(Random==0){
            output="Rock";
        }
        else if(Random==1){
            output="Paper";
        }
        else if(Random==2){
            output="Scissors";
        }



        while(true){
            if(Random==0 && user==0 || Random==1 && user==1 || Random==2 && user==2 ){
                System.out.printf("it Draw   COM Picks-%s",output);
                break;
            }
            else if(Random==0 && user==2 || Random==2 && user==1 || Random==1 && user==0 ){
                System.out.printf("You Lose   COM Picks-%s",output);

                break;
            }
            else if(Random==2 && user==0 || Random==1 && user==2 || Random==0 && user==1 ){
                System.out.printf("You win   COM Picks-%s",output);

                break;
            }
        }   

    }
}
