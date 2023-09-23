public class _07_pr_02_Funtions_Star_Pattern {
    
    static void Star(int x){
        for(int i=0;i<=x;i++){
            for(int j=0;j<i;j++){
             System.out.print("*");
 
            }
            System.out.print("\n");
         }
    }
    public static void main(String[] args) {
        int Num_star=4;
        Star(Num_star);
    }
}
