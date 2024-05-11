abstract class Prarent{
    public Prarent(){
        System.out.printf("I am a contractor\n");
    }
    abstract public void Greet();
}
class Child extends Prarent{
    @Override
    public void Greet(){
        System.out.printf("Greeting From Child Class");
    }
}
abstract class Child2 extends Prarent{
    public void Wellcome(){
        System.out.printf("Wellcome From Child2 Class");
    }
}

public class _11_Abstract {
 public static void main(String[] args) {
    Child object = new Child(); // it will work
    // Child2 object2 = new Child2(); // Abstract Class cant be object

    object.Greet();
 }
    
}