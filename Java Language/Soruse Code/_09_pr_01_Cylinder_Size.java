class Cylinder{
    private float Radius;
	private float Height;

    public float getnum1(){
        return Radius;
    }

    public float getnum2(){
        return Height;
    }

    public void setnum1(float user){
        Radius=user;
    }
    public void setnum2(float user){
        Height=user;
    }

    public float Size(){
        float pi = 3.1416f;
        float r=Radius*Radius;
        float formula=pi*r*Height;
        return formula;
     }


}


public class _09_pr_01_Cylinder_Size {
    public static void main(String[] args) {
        Cylinder object = new Cylinder();

        object.setnum1(2.0f);
        object.setnum2(5.0f);

        System.out.printf("%f",object.Size());

    }
}
