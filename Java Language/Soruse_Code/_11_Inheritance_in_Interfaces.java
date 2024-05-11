interface Format1{
    void Serial1();
    void Serial2();
}
interface Format2 extends Format1{
    void Movie1();
    void Movie2();
}
class Prarent implements Format2{
    @Override
    public void Movie1() {
        System.out.printf("Movie1\n");
    }
    @Override
    public void Movie2() {
        System.out.printf("Movie2\n");
    }
    @Override
    public void Serial1() {
        System.out.printf("Serial1\n");
    }
    @Override
    public void Serial2() {
        System.out.printf("Serial2\n");
    }
}

public class _11_Inheritance_in_Interfaces {
    public static void main(String[] args) {
        Prarent object = new Prarent();

        object.Movie1();
                object.Movie2();

    }
    
}