public class _05_Break_Continue_Statement {
    public static void main(String[] args) {
        
        for(int i=10;i>0;i--){  
            if(i==5){  
                continue;//continue skips the rest statement
            }
            else if(i==3){
                break; // It will exit the loop
            }  
            System.out.println(i);
            
        }
    }
}
