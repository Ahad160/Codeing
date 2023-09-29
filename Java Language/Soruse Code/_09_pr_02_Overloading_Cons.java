class rectangle{
    public rectangle(){
        int lenth=9;
        int Height=8;
        System.out.printf("%d",lenth+Height);//PPP
    }

    public rectangle(int user,int user2){
        int lenth=user;
        int Height=user2;

        System.out.printf("lenth is %d And Height is %d\n",lenth,Height);
    }

    public void PPP(){
        //PPP
    }


}

public class _09_pr_02_Overloading_Cons {
    public static void main(String[] args) {
        rectangle object = new rectangle(4,5);

        object.PPP(); //PPPs
        
    }
}
