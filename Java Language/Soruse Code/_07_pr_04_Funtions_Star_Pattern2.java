public class _07_pr_04_Funtions_Star_Pattern2 {

    static void Star(int x){
        for(int i=x;i>0;i--){
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
    

