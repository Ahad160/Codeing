import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;



public class _15_DateTimeFormatter {
    public static void main(String[] args) {
        LocalDateTime object = LocalDateTime.now();

        DateTimeFormatter objectformatter = DateTimeFormatter.ofPattern("dd-MM-yyyy");

        String MyDate = object.format(objectformatter);

        System.out.println(MyDate);
    }
}
