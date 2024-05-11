public class _07_pr_06_Average_Number_Argument {

    static int Average(int ...arr){
        int sum=0;
        for (int element:arr){
            sum+=element;
        }
        
        return (sum/arr.length);
    }
    public static void main(String[] args) {
        System.out.printf("%d",Average(1,2,3,4,5,6));
    }
}
