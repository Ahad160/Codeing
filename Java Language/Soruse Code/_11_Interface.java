interface Format{
    int pin=55; //Variable As Final
    void Name();
    void Address();
}

interface Format2{
    
}
class Prarent implements Format{
    @Override
    public void Name() {
        System.out.printf("My Name is Raiden\n");
    }
    @Override
    public void Address() {
        System.out.printf("My Address is Earth\n");
    }
}

public class _11_Interface {
    public static void main(String[] args) {
        Prarent object = new Prarent();

        object.Name();
        // System.out.printf("%d",object.pin);
    }
}
