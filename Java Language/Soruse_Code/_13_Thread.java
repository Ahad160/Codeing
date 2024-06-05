class Thread_Info_1 extends Thread{
    @Override
    public void run(){
        while (true) {
            System.out.printf("Process 1 is Running\n");
            System.out.printf("\n");

        }
    }
}

class Thread_Info_2 extends Thread{
    @Override
    public void run(){
        while (true) {
            System.out.printf("Process 2 is Running\n");
            System.out.printf("\n");

        }
    }
}

public class _13_Thread {
    public static void main(String[] args) {
        Thread_Info_1 object1 = new Thread_Info_1();
        Thread_Info_2 object2 = new Thread_Info_2();


        object1.start();
        object2.start();


    }
}
