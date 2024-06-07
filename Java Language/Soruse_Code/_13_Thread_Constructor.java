class Thread_Info extends Thread{
    public Thread_Info (String Name){
        super(Name);
    }
    public void run(){
        System.out.printf("Thread");
    }
}


public class _13_Thread_Constructor {
    public static void main(String[] args) {
        Thread_Info object = new Thread_Info("Raiden");
        object.start();

        System.out.printf("The Thread ID is %d",object.getId());
        System.out.printf("The Name is ID is %s",object.getName());

    }
}
