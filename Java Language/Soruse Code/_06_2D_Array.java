public class _06_2D_Array {
    public static void main(String[] args) {
        int Arrays[][] = new int[2][3];

        Arrays[0][0] = 101;
        Arrays[0][1] = 102;
        Arrays[0][2] = 103;
        Arrays[1][0] = 201;
        Arrays[1][1] = 202;
        Arrays[1][2] = 203;

        for (int i = 0; i < Arrays.length; i++) {
            for (int j = 0; j < Arrays[i].length; j++) {
                System.out.printf("%d",Arrays[i][j]);
                System.out.print(" ");
                
            }
            System.out.printf("\n");
        }

    }
}
