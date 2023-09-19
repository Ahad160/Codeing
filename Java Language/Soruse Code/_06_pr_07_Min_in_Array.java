public class _06_pr_07_Min_in_Array {
    public static void main(String[] args) {
        int value[]={10,20,99};

        int max=Integer.MAX_VALUE;

        for(int element:value){
            if(element>max){
                max=element;
            }
        }
        System.out.printf("The Highest is %d\n",max);
    }
}
