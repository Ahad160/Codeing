interface Airtel{
    void Call();
    void Internet();
    void SMS();
}
interface Camera{
    void Click_Image();
    void Record_Video();
}


class smartphone implements Airtel,Camera{
    @Override
    public void Call() {
        System.out.printf("Calling\n");
    }
    @Override
    public void Internet() {
        System.out.printf("Useing Internet");
    }
    @Override
    public void SMS() {
        System.out.printf("SMSing someone\n");
    }
    @Override
    public void Click_Image() {
        System.out.printf("Say Cheege\n");
    }
    @Override
    public void Record_Video() {
        System.out.printf("Recording Video\n");
    }
}

public class _11_Polymorphism_In_Interfaces {
    public static void main(String[] args) {
        Camera object = new smartphone();
        object.Click_Image(); // You can access only the reference interface

        smartphone object_2 = new smartphone();
        object_2.Internet();   // You can use all mothod in class if you reffer class object
    }
}
