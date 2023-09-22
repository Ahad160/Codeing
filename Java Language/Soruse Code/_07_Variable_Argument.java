public class _07_Variable_Argument {

    static int sum(int ...arr){
        int result=0;
        for(int a:arr){
            result+=a;
        }
        return result;

    }
    public static void main(String[] args) {
        System.out.printf("1+2=%d\n",sum(1,2));
        System.out.printf("1+2+3=%d\n",sum(1,2,3));
        System.out.printf("1+2+3+4=%d\n",sum(1,2,3,4));


    }
    
}