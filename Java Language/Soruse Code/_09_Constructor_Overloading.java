class Overloading{
    int A;

    public Overloading(){

        System.out.printf("Construcing Overloading\n");
    }

    public Overloading(int u1,String u2){

        System.out.printf("Heloo Guys is defult constractor\n");
        System.out.printf("Roll is %d And name is %s",u1,u2);
    }
}

public class _09_Constructor_Overloading {
    public static void main(String[] args) {
        Overloading object = new Overloading(12,"Alpha");
                // Overloading object = new Overloading();

        object.A=1;
    }


}   
