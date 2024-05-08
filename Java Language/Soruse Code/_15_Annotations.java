@FunctionalInterface
interface Number{
    void F1();
    // void F2(); // not Allow

}
class Parent{
    
    public void Funtion(){
        System.out.printf("Parent Class");
    }
}
class Child extends Parent{
    @Override
    public void Funtion(){
        System.out.printf("Child Class\n");
    }
    @Deprecated
    public void CallMe(){
        System.out.printf("Call Me\n");

    }
}
public class _15_Annotations {

    @SuppressWarnings("deprecation")
    public static void main(String[] args) {
        Child Object = new Child();

        Object.Funtion();

        Object.CallMe();
    }
}
