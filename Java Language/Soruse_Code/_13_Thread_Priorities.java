class Thread_Info extends Thread{
    public Thread_Info (String Name){
        super(Name);
    }
    public void run(){
        while (true) {
            System.out.println("Thread Name is " + getName());
            
        }
    }
}

public class _13_Thread_Priorities {
    public static void main(String[] args) {
        Thread_Info object1 = new Thread_Info("Raiden1");
        Thread_Info object2 = new Thread_Info("Raiden2");
        Thread_Info object3 = new Thread_Info("Raiden3");
        Thread_Info object4 = new Thread_Info("Raiden4 [Is Most Importent]");

        //set Priorites
        object4.setPriority(Thread.MAX_PRIORITY);


        object1.start();
        object2.start();
        object3.start();
        object4.start();

    }
    
}