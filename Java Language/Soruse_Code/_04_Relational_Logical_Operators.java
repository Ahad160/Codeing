public class _04_Relational_Logical_Operators {
    public static void main(String[] args) {
        int num =5;
        int num2 =56;

        boolean Values = true;

        if(num==5 && num2==56){
            System.out.print("Num and Num2 Values Are Matched\n");            
        }
        else if(num==5 || num2==98){
            System.out.println("OR Opearator is Runed");
        }
        //Not operator
        System.out.println(!Values);

    }
}
