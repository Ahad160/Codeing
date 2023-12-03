abstract class Pen{
    abstract public void changeNib();
}

class FountainPEN extends Pen{
    @Override
    public void changeNib(){
        System.out.printf("Changeing The Nib\n");
    }
}
public class _11_pr_02_Additional_Method {
    public static void main(String[] args) {
        FountainPEN obejct = new FountainPEN();
        obejct.changeNib();
    }
}
