public class _06_pr_01_Array_Sum {
    public static void main(String[] args) {
        float value [] = {10.0f,20.0f,30.0f,40.0f,50.f};
        float sum=0;

        for(float element:value){
            sum+=element;
        }

        System.out.printf("The Sum of Array is %f",sum);
    }
}




