import java.util.*;

public class _15_LinkedList {
    public static void main(String[] args) {
        LinkedList<Integer> object = new LinkedList<>();

        object.add(1);
        object.add(3);
        object.add(5);
        object.add(7);

        for (int index = 0; index < object.size(); index++) {
            System.out.printf("%d\n",object.get(index));
        }

        System.out.printf("%s",object.contains(22));
    }
    
}