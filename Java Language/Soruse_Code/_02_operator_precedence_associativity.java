public class _02_operator_precedence_associativity {
    public static void main(String[] args) {
        // Precedence & Associativity

        //int a = 6*5-34/2;
        /*
        Highest precedence goes to * and /. They are then evaluated on the basis
        of left to right associativity
            =30-34/2
            =30-17
            =13
         */
        //int b = 60/5-34*2;
        /*
            = 12-34*2
            =12-68
            =-56
         */

        //System.out.println(a);
        //System.out.println(b);

        // Quick Quiz
        int x=20;
        int y=10;

        int a=5;
        int b=6;
        int c=7;

        int Q1=(x-y)/2;
        int Q2=(b*b-4*a*c)/(2*a);

        System.out.println(Q1);
        System.out.println(Q2);
    
    }
}