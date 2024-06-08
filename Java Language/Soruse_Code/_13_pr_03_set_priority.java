class Thread1 extends Thread{
    public void run(){
        int A=0;
        while(A<100){
            System.out.printf("Thread 1 Runing\n");
            System.out.printf("\n");
            A++;
        }
    }
}

class Thread2 extends Thread{
    public void run(){
        while(true){
            System.out.printf("Thread 2 Runing\n");
            System.out.printf("\n");
        }

    }
}
public class _13_pr_03_set_priority {
    public static void main(String[] args) {
        Thread1 object1 = new Thread1();
        Thread2 object2 = new Thread2();

        // Set Priority
        object1.setPriority(5);
        object1.setPriority(9);

        // Show Priority
        System.out.printf("%d\n",object1.getPriority());
        System.out.printf("%d\n",object2.getPriority());


        object1.start();
        object2.start();

        // Thread State check
        System.out.printf("%s\n",object1.getState());
        System.out.printf("%s\n",Thread.currentThread().getState());



    }
}
