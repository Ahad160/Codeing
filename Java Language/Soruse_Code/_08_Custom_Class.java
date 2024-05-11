
class Details{
    int id;
    String name;

    public void info(){
        System.out.printf("Youer Name is %s\n and Youer ID is %d\n",name,id);
    }
}

public class _08_Custom_Class {

    public static void main(String[] args) {
        Details object = new Details();  // Creating First Object
        Details object_2 = new Details(); // Creating Secend Object

        object.id=500;
        object.name="Raiden";

        object_2.id=60;
        object_2.name="John";

        object.info();

        object_2.info();



    }
}