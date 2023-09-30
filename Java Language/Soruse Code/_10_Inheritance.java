class Prarnet{
    int user_id=774;
    int user_PID=7781;

    public void show(){
        System.out.printf("This is a void Funtionsn\n");
    }
}

class Child extends Prarnet {
    public void output(){
        System.out.printf("%d\n",user_PID);
                System.out.printf("%d\n",user_id);

    }
}
public class _10_Inheritance {

    public static void main(String[] args) {
        Child object = new Child();

        object.output();
        object.show();
    }
}