import java.util.Arrays;

public class MaxCell {
    public static int max_cell(int[][] grid, int rows, int cols) {
        int res = 0;
        int[][] vis = new int[rows][cols];

        for(int i = 0; i < rows; ++i) {
            for(int j = 0; j < cols; ++j) {
                res = Math.max(res, blob(grid, vis, i, j, rows, cols));
            }
        }

        return res;
    }

    public static int blob(int[][] g, int[][]v, int r, int c, int rows, int cols) {
        int res = 0;

        if(r < rows && r >= 0 && c < cols && c >= 0 && g[r][c] > 0 && v[r][c] == 0) {
            v[r][c] = 1;
            res += g[r][c];
            res += blob(g, v, r+1, c, rows, cols);
            res += blob(g, v, r-1, c, rows, cols);
            res += blob(g, v, r, c+1, rows, cols);
            res += blob(g, v, r, c-1, rows, cols);
            return res;
        }
        else {
            return res;
        }
    }

    public static void main(String args[]) {
        int[][] multi = new int[][]{
            {1, 2, 0, 4},
            {3, 0, 0, 5},
            {0, 10, 0, 0},
            {0, 8, 7, 6}
        };

        int result = max_cell(multi, 4, 4);
        System.out.println(result);
    }
}
