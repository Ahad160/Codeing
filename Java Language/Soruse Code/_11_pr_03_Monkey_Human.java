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

public class _11_pr_03_Monkey_Human {
    public static void main(String[] args) {
        Human obejct = new Human();
        obejct.Bite();
        obejct.Eats();
        obejct.Sleep();
        obejct.jump();
    }
}
