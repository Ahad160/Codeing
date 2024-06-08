class Thread_Info1 extends Thread{
    public void run(){
        int A=0;
        while (A<1000) {
            System.out.println("Thread 1 in Runing");

            try {
                Thread.sleep(400);   // Sleep For 400 m/s
                
            } catch (Exception e) {
                System.out.printf("%s",e);
            }
            A++;
        }
    }
}

class Thread_Info2 extends Thread{
    public void run(){
        int B=0;
        while (B<1000) {
            System.out.println("Thread 2 in Runing");
            B++;
            
        }
    }
}

public class _13_Thread_Method {
    public static void main(String[] args) {
        Thread_Info1 object1 = new Thread_Info1();
        Thread_Info2 object2 = new Thread_Info2();

        object1.start();

        // try {
        //     object1.join();  //Thread 2 will not start until the Thread 1 is Finished
        // } catch (Exception e) {
        //    System.out.printf("%s",e);
        // }

        object2.start();

    }
}
