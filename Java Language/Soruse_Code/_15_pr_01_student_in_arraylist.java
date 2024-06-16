import java.util.*;

public class _15_pr_01_student_in_arraylist {
    public static void main(String[] args) {
        ArrayList<String> object = new ArrayList<>();

        object.add("Rezwan");
        object.add("Harry");
        object.add("Jubaeid");
        object.add("Mahi");
        object.add("Raiden");

        for (int i=0;i<object.size(); i++) {
            System.out.printf("%s\n",object.get(i));
        }
    }
}
