public class _07_pr_07_Celsius_Fahrenheit {
    static float Convert(float x){
        float formula= (x*9/5)+32;
        return formula;
    }
    public static void main(String[] args) {
        float Celsius=5.0f;
       
        System.out.printf("%f",Convert(Celsius));
    }
}
