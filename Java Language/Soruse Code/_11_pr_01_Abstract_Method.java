abstract class Pen{
    abstract public void Write();
    abstract public void Refil();
}

class Prarent extends Pen{
    @Override
    public void Write() {
        System.out.printf("I am Writeing\n");
    }
    @Override
    public void Refil() {
        System.out.printf("Refil The Pen\n");
    }
}

public class _11_pr_01_Abstract_Method {
    public static void main(String[] args) {
        Prarent object = new Prarent();
        object.Refil();
    }    
}
