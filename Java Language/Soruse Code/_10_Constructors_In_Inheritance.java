class Prarent{
    public Prarent(){
        System.out.printf("THIS is a Constractor\n");
    }

}

class Child extends Prarent{
    
}

public class _10_Constructors_In_Inheritance {

    public static void main(String[] args) {
        Child Object = new Child();
    }
}