class Prarent{
    int a;
    Prarent(int a){
        this.a = a;
    }

    public int get(){
        return a;
    }
}


public class _10_This {
    public static void main(String[] args) {
        Prarent object = new Prarent(70);
        System.out.printf("%d",object.get());

    }
}
