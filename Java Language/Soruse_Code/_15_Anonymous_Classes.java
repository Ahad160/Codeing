interface Democlass {
    void F1();
    void F2();
}

public class _15_Anonymous_Classes {
    public static void main(String[] args) {
        Democlass object = new Democlass() {
            @Override
            public void F1() {
                System.out.println("F1 Running");
            }

            @Override
            public void F2() {
                System.out.println("F2 Running");
            }
        };

        object.F1();
        object.F2();
    }
}
