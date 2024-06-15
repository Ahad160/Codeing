import java.util.*;
public class _15_GregorianCalendar {
    public static void main(String[] args) {
        GregorianCalendar object = new GregorianCalendar();

        System.out.println(object.isLeapYear(2025));

        System.out.println(TimeZone.getAvailableIDs()[0]);
        System.out.println(TimeZone.getAvailableIDs()[2]);
        System.out.println(TimeZone.getAvailableIDs()[1]);

    }    
}