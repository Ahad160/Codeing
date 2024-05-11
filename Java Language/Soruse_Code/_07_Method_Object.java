public class _07_Method_Object {

    int Method(int x,int y){
        int z;
        z=x+y;
        return z;
    }
    public static void main(String[] args) {
        
        _07_Method_Object object = new _07_Method_Object(); // Object Creatings
        int a=5;
        int b=9;

        System.out.printf("%d\n",object.Method(a,b));
    }
}
