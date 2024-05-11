import java.util.Scanner;

public class _04_pr_04_Day_Date {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter Date-");
        int Date = input.nextInt();
        input.close();
        

        if(Date==1 || Date==8 || Date==15 || Date==22 || Date==29 ){
            System.out.println("SUN Day");
        }
        else if(Date==2 || Date==9 || Date==16 || Date==23 || Date==30){
            System.out.println("MON Day");

        }
        else if(Date==3 || Date==10 || Date==17 || Date==24 || Date==31){
            System.out.println("TUE Day");

        }
        else if(Date==4 || Date==11 || Date==18 || Date==25 ){
            System.out.println("WED Day");

        }
        else if(Date==5 || Date==12 || Date==19 || Date==26){
            System.out.println("THU Day");

        }
        else if(Date==6 || Date==13 || Date==20 || Date==27){
            System.out.println("FRI Day");

        }
        else if(Date==7 || Date==14 || Date==21 || Date==28){
            System.out.println("SAT Day");

        }


    }
}
