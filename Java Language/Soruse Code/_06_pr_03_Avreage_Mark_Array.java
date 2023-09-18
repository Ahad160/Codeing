public class _06_pr_03_Avreage_Mark_Array {
    public static void main(String[] args) {
        int Array[] ={50,60,70,80,90,10};
        int sum=0;

        for(int element:Array){
            sum=+element;    
        }

        float Average = sum/5;

        System.out.printf("The Average of All student Mark in Physics is %f",Average);

    }
}
