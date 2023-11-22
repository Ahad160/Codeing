abstract class Prarent{
    public Prarent(){
        System.out.printf("I am a contractor\n");
    }
    abstract public void Greet();
}
abstract class Child extends Prarent{
    @Override
    public void Greet(){
        System.out.printf("Greeting From Child Class");
    }
}

public class _11_Abstract {
 public static void main(String[] args) {
    
 }
    
}