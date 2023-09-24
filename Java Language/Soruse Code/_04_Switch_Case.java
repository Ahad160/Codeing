public class _04_Switch_Case {
    public static void main(String[] args) {
        int Battery=90;

        switch(Battery){
            case 90:
                System.out.println("Battery is 90%");
                break;

            case 80:
                System.out.println("Battery is 80%");
                break;

            case 70:
                System.out.println("Battery is 70%");
                break;    
            
            default:
                System.out.println("Battery is Full");
                System.out.printf("");
        }
    }
    
}