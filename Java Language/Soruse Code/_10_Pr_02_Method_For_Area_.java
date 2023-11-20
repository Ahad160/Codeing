class Circle{
    int value;
    public Circle(int value){
        this.value=value;
    }
    public double Circle_Size(){
        double forumal = Math.PI*(value*value);
        return forumal;
    }

}
class Cylinder{
    int Height;
    int Radius;
    public Cylinder(int V1,int V2){
        this.Height=V1;
        this.Radius=V2;

    }
    
    public double Area(){
        double forumal = Math.PI*(Radius*Radius);
        return forumal;
    }
    public double Volume(){
        double forumal2=Area()*Height;
        return forumal2;
    }
}
public class _10_Pr_02_Method_For_Area_ {
    public static void main(String[] args) {
        int Radius=7;
        int Height=5;

        // Circle object = new Circle(Radius);
        // System.out.printf("The Circle of Area is %f\n",object.Circle_Size());

        Cylinder object2 = new Cylinder(Height,Radius);
        System.out.printf("The Cylinder of Area is %f and Volume is %f",object2.Area(),object2.Volume());

    }
}
