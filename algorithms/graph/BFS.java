import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;


public class BFS {
    // This is how I go to my neighbors.
    public static final int[] DX = {0, 0, -1, 1};
    public static final int[] DY = {-1, 1, 0, 0};

    public static void main(String[] Args) {
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();

        // For bfs, we need visited and the graph (grid).
        boolean[][] visited = new boolean[n][n];
        int[][] grid = new int[n][n];

        // Parse.
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                grid[i][j ] = scan.nextInt();
            }
        }

        // Looking for max blob.
        int max = -1;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                // We've seen it, or we can't go there.
                if (visited[i][j] || grid[i][j] == 0)
                    continue;
                // Update.
                max = Math.max(max, bfs(i, j, n, grid, visited));
            }
        }
        System.out.println(max);
    }

    public static int bfs(int x, int y, int n, int[][] grid, boolean[][] visited) {
        int result = 0;

        Queue<Integer> qx = new LinkedList<>();
        Queue<Integer> qy = new LinkedList<>();

        // We haven't seen it before, now we have.
        visited[x][y] = true;
        qx.add(x);
        qy.add(y);

        // While we have stuff to do.
        while (qx.size() > 0) {
            int current_x = qx.remove();
            int current_y = qy.remove();

            // Add the cell to the blob.
            result += grid[current_x][current_y];

            // Go through neighbors.
            for (int i = 0; i < 4; ++i) {
                // Coordinate of my neighbor.
                int new_x = current_x + DX[i];
                int new_y = current_y + DY[i];

                // Anything invalid.
                if (new_x < 0 || new_x >= n)
                    continue;
                else if (new_y < 0 || new_y >= n)
                    continue;
                else if (visited[new_x][new_y] || grid[new_x][new_y] == 0)
                    continue;

                // This cell is valid, lets do more work.
                visited[new_x][new_y] = true;
                qx.add(new_x);
                qy.add(new_y);
            }
        }

        return result;
    }
}
