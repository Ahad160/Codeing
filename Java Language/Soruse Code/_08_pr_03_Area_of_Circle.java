class Area{
    float user=7f;
    public float calculating(){
        float pi = 3.141592653f;
        return pi*(user*user);
    }
}

public class _08_pr_03_Area_of_Circle {
    public static void main(String[] args) {
        Area object = new Area();
        
        System.out.printf("%f",object.calculating());
        
    }
    
}