class Solution {
    public int[][] solve(int[][] matrix) {
        for(int i = 0; i < matrix.length; i++){
            for(int j = i;  j < matrix.length; j++){
                int temp = 0;
                temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for(int j = 0; j < matrix.length; j++){
            for(int i = 0; i<matrix.length / 2; i++){
                int temp = 0;
                temp = matrix[i][j];
                matrix[i][j] = matrix[matrix.length - 1 - i][j];
                matrix[matrix.length - 1 - i][j] = temp;
            }
        }        return matrix;
    }
}
