class Parant{
    public void greet(){
        System.out.printf("Good Morning\n");
    }
    public void Serve(){
        System.out.printf("Good Morning From Parant Class\n");
    }
}
class Child extends Parant{
    public void welcome(){
        System.out.printf("Welcomeing\n");
    }
    public void Serve(){
        System.out.printf("Good Morning From Child Class\n");
    }
}
public class _10_Dynamic_Method_Dispatch {

    public static void main(String[] args) {
        // Child object = new Child(); // Allowed
        // object.Serve(); // Allowed

        Parant object = new Child();
        object.Serve();
        // object.welcome(); //Not  Allowed
        
        // Child object = new Parant(); //Not  Allowed
    }
}