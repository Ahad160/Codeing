public class _07_pr_03_Recursive_Natural_Sum {
    static int Recursive(int x){
        if (x==0){
            return 1;
        }
        else{
            return x+Recursive(x-1);
        }
    }
    public static void main(String[] args) {
        int Natural_Number=10;

        System.out.printf("%d",Recursive(Natural_Number)); 
    }
}
