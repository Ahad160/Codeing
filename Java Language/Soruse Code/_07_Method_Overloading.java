public class _07_Method_Overloading {
    static void Funtion(){
        System.out.printf("Just a simple Funtion");

    }
    static void Funtion(int user){
        System.out.printf("%d\n",user);
    }
    
    
    public static void main(String[] args) {
        Funtion(50);

        Funtion();
    }
    
}