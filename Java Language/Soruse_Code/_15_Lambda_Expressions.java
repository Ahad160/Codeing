@FunctionalInterface
interface LamdaFun{
    void F1();
}

public class _15_Lambda_Expressions {
    public static void main(String[] args) {
        LamdaFun object = ()->{System.out.printf("Lamda Method");};

        object.F1();
    }
}
