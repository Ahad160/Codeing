class Runnable_Thread1 implements Runnable{
    public void run(){
        while(true){
            System.out.printf("Runnable Thread 1 Runing\n");
            System.out.printf("\n");
        }
    }
}

class Runnable_Thread2 implements Runnable{
    public void run(){
        while(true){
            System.out.printf("Runnable Thread 2 Runing\n");
            System.out.printf("\n");
        }

    }
}

public class _13_Runnable_Thread {

    public static void main(String[] args) {
        Runnable_Thread1 object1 = new Runnable_Thread1();
        Thread object_Thread1 = new Thread(object1);
        
        Runnable_Thread2 object2 = new Runnable_Thread2();
        Thread object_Thread2 = new Thread(object2);

        object_Thread1.start();
        object_Thread2.start();



    }
}