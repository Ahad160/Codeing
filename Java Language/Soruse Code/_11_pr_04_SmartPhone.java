abstract class TelePhone{
    abstract void Ring();
    abstract void Pick();
    abstract void Disconnected();
}
class SmartPhone extends TelePhone{
    @Override
    void Ring() {
        System.out.printf("Phone is Ringing\n");
    }
    @Override
    void Pick() {
        System.out.printf("Call is Picked\n");
    }
    @Override
    void Disconnected() {
        System.out.printf("Call Disconnected\n");
    }
    public void Anwser_CAll(){
        System.out.printf("Answer The Call\n");
    }
}
public class _11_pr_04_SmartPhone {
    public static void main(String[] args) {
        TelePhone object = new SmartPhone();
        object.Disconnected();

        SmartPhone object_2 = new SmartPhone();
        object_2.Anwser_CAll(); // Now you can access the smartphone body method
    }
}
