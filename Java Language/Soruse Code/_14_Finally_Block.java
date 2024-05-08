public class _14_Finally_Block {
    public static void main(String[] args) {
        try {
            int  A= 5;
            int  B= 0;
            int  c=A/B;
        } catch (Exception Error) {
            System.out.println(Error);
        }
        finally{
            System.out.printf("It is finally over\n");
        }
    }
}
