class Monkey{
    void jump(){
        System.out.printf("Monkey Jump\n");
    }
    void Bite(){
        System.out.printf("Mokey Bite\n");
    }
}
interface Basic_Animal{
    void Eats();
    void Sleep();
}
class Human extends Monkey implements Basic_Animal{
    @Override
    public void Eats(){
        System.out.printf("Moneky Love Banana\n");
    }
    @Override
    public void Sleep() {
        System.out.printf("Monkey Alawys Sleep\n");
    }
}
public class _11_pr_05_Monkey_Polymorphism {
    public static void main(String[] args) {
        Basic_Animal object = new Human();

        object.Sleep();
    }
}
