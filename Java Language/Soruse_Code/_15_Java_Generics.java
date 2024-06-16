import java.util.ArrayList;

public class _15_Java_Generics {
    public static void main(String[] args) {
        ArrayList object = new ArrayList();

        object.add(54);
        object.add(154);

        int a = (int) object.get(0);
        System.out.printf("%d",a);
    }
}
