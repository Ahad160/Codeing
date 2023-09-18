public class _06_pr_04_Add_Two_Array {
    public static void main(String[] args) {
        int Array [][] = {{1,2,3},
                          {4,5,6}};

        int Array2 [][] = {{1,2,3},
                           {4,5,6}};

        int [][] result = {{0, 0, 0},
                          {0, 0, 0}};



    for (int i = 0; i < Array.length; i++) {
        for (int j = 0; j < Array2[i].length; j++) {
        System.out.format(" Setting value for i=%d and j=%d\n", i, j);
        result[i][j] = Array[i][j] + Array2[i][j];
       }
    }
    }
}
