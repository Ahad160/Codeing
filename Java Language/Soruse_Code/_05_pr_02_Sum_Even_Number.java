public class _05_pr_02_Sum_Even_Number {
    public static void main(String[] args) {
        int n=1;
        int sum =0;

        while (n<10) {
            if(n%2==0){
                sum=sum+n;
            }
            n++;
        }

        System.out.printf("Sum of Even Number is %d",sum);
    }
    
}
