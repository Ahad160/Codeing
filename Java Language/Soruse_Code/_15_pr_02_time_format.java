import java.util.*;

public class _15_pr_02_time_format {
    static int hrs=50;
    static int min=50;
    static int sec=50;

    public static void main(String[] args) {
        Date object = new Date();

        System.out.println(object.getHours() + ":" + object.getMinutes() + ":" + object.getSeconds());

    }
}
