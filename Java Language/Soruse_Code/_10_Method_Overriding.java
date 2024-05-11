class Parent{
    public void Funtion(){
        System.out.printf("I am Funtion1 From Class Parent");
    }
}


class Child extends Parent{
    @Override
    public void Funtion(){
        System.out.printf("I am Funtion1 From Class Child");
    }
}
public class _10_Method_Overriding {

    public static void main(String[] args) {
        Child object = new Child();

        object.Funtion();
    }
}