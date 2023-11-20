class Rectangle{

    int Length;
    int Width;
    int height;
    public Rectangle(int V1,int V2,int V3){
        this.Length=V1;
        this.Width=V2;
        this.height=V3;
    }
    public double Area(){
        double forumal = Length*Width;
        return forumal;
    }
    public double Volume(){
        double forumal2 = Length*Width*height;
        return forumal2;
    }

}
class Cuboid{
    int Length;
    int Width;
    int height;

    public Cuboid(int V1,int V2,int V3){
        this.Length=V1;
        this.Width=V2;
        this.height=V3;
    }
    
    public double Area(){
        double forumal = Length*Width;
        return forumal;
    }
    public double Volume(){
        double forumal2 = Length*Width*height;

        return forumal2;
    }
}
public class _10_pr_03_Area_Getter_Setter {
    public static void main(String[] args) {
        
    
        int Length=5;
        int Width=5;
        int height=7;

        Rectangle object = new Rectangle(Length,Width,height);
        System.out.printf("The Rectangle of Area is %f And Volume is %f\n",object.Area(),object.Volume());

        Cuboid object2 = new Cuboid(Length,Width,height);
        System.out.printf("The Cuboid of Area is %f And Volume is %f",object2.Area(),object2.Volume());
    }
}
