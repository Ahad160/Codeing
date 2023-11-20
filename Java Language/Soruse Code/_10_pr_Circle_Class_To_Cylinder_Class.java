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
class Cylinder extends Circle{
    int Height=5;
    public  Cylinder(int v){
        super(v);
    }
    public double Cylinder_Size(){
        double forumal = Math.PI*(this.value*this.value)*Height;
        return forumal;
    }
}

public class _10_pr_Circle_Class_To_Cylinder_Class {
    public static void main(String[] args) {
        int Radius=7;
        int Height=5;

        Circle object = new Circle(Radius);
        System.out.printf("The Circle of Area is %f\n",object.Circle_Size());

        Cylinder object2 = new Cylinder(Height);
        System.out.printf("The Cylinder of Area is %f",object2.Cylinder_Size());


    }
}
