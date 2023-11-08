class Prarent{
    public Prarent(){    //Constrator
        System.out.printf("This is a Constractor \n");     
    }
    public void Funtion1(){
            System.out.printf("This is a Funtions1\n");
    }
    public void Funtion2(){
            System.out.printf("This is a Funtions2\n");
    }
    
}

class Child extends Prarent{

    public Child(int user){     //Constrator
            super();
            System.out.printf("This is a child constractor and %d\n",user);
    }

    public void Funtion3(){
            System.out.printf("This is a Funtions3\n");
    }
}

public class _10_Super {

    public static void main(String[] args) {
        // Prarent object = new Prarent();
        Child object2 = new Child(7);

        object2.Funtion1();

        
      
    }
}