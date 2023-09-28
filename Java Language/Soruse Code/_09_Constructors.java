class Prarent{

    int a=23; //For No resoan

    public Prarent(int u1,String u2){

        System.out.printf("Heloo Guys is defult constractor\n");
        System.out.printf("Roll is %d And name is %s",u1,u2);


    }
    
}


public class _09_Constructors {
    public static void main(String[] args) {
        int Roll=984534;
        String name ="iren";
        Prarent object = new Prarent(Roll,name);

        object.a=2;//For No resoan
        
    }   
}
