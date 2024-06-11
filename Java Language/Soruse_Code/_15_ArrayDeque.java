import java.util.*;
public class _15_ArrayDeque {
    public static void main(String[] args) {
        ArrayDeque<Integer> object = new ArrayDeque<>();

        object.add(50);
        object.add(20);
        object.addFirst(3);
        System.out.printf("%d\n",object.getFirst());
        System.out.printf("%d\n",object.getLast());


    }
}
