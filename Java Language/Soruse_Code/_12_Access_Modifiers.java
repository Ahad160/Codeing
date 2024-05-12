class C1{
    public int Code=555;
    protected char CName= 'A';
    private String User= "Raiden";
}
class C2 extends C1{
    
}

public class _12_Access_Modifiers {
    public static void main(String[] args) {
        C2 object = new C2();

        System.out.printf("%s\n",object.CName);
        System.out.printf("%s\n",object.User); // Can't Access

    }
}
