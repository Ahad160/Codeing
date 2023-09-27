class Details{
    private int num;
    private String name;

    public String system(){
      return name;
    }

    public int getnum(){
        return num;
    }
    public void setnum(int n){
        num=n;
    }

}


public class _09_Getter_Setter {

    public static void main(String[] args) {
        Details object  = new Details();

        object.setnum(500);

        System.out.printf("%d",object.getnum());
    }
}