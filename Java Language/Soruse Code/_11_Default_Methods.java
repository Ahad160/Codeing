
interface War{
    void Guns();
    void Tank();
    void Plane();

    default void submarine(){
        System.out.printf("Submarine is Diveing in Water\n");
    }
    
}

class country implements War{
    @Override
    public void Guns() {
        System.out.printf("Gun is Openfire\n");
    }
    @Override
    public void Tank() {
        System.out.printf("Tank is Clearing Aeras\n");
    }
    @Override
    public void Plane() {
        System.out.printf("Plane Are Fireing Missaile\n");
    }
}

public class _11_Default_Methods {
    public static void main(String[] args) {
        country object = new country();

        object.Guns();
        object.Tank();
        object.Plane();
        object.submarine();
    }
    
}