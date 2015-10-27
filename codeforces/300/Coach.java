import java.util.Scanner;
import java.util.HashSet;
import java.util.ArrayList;

public class Coach {
    static boolean[][] adj = new boolean[50][50];
    static boolean[] vis = new boolean[50];
    static HashSet<Integer> free = new HashSet<>();
    static ArrayList<ArrayList<Integer> > teams = new ArrayList<>(); 
    static int N;

    public static void dfs (int u, ArrayList<Integer> result) {
        vis[u] = true;
        result.add(u);
        for (int v = 1; v <= N; ++v) {
            if (adj[u][v] && !vis[v])
                dfs(v, result);
        }
    }

    public static void main (String[] args) {
        Scanner scan = new Scanner(System.in);

        N = scan.nextInt();
        int m = scan.nextInt();
        boolean canDo = true;

        for (int i = 1; i <= N; ++i)
            free.add(i);

        for (int i = 0; i < m; ++i) {
            int u, v;

            u = scan.nextInt();
            v = scan.nextInt();

            if (free.contains(u))
                free.remove(u);

            if (free.contains(v))
                free.remove(v);

            adj[u][v] = true;
            adj[v][u] = true;
        }

        for (int u = 1; u <= N; ++u) {
            if (vis[u] || free.contains(u))
                continue;

            ArrayList<Integer> result = new ArrayList<>();
            dfs(u, result);

            if (result.size() < 3 && free.size() > 0) {
                ArrayList<Integer> fromFree = new ArrayList<>();
                for (int v: free) {
                    fromFree.add(v);
                    if (result.size()+fromFree.size() == 3)
                        break;
                }
                for (int v: fromFree) {
                    result.add(v);
                    vis[v] = true;
                    free.remove(v);
                }
            }

            if (result.size() != 3)
                canDo = false;
            
            /* System.out.println(result); */
            teams.add(result);
        }

        if (free.size() > 0) {
            if (free.size() % 3 == 0) {
                ArrayList<Integer> freeList = new ArrayList<>(free);
                for (int i = 2; i < freeList.size(); i += 3) {
                    ArrayList<Integer> tmp = new ArrayList<>();
                    tmp.add(freeList.get(i));
                    tmp.add(freeList.get(i-1));
                    tmp.add(freeList.get(i-2));
                    teams.add(tmp);
                }
            }
            else
                canDo = false;
        }

        if (canDo) {
            for (ArrayList<Integer> team: teams) {
                System.out.println(team.get(0) + " " + team.get(1) + " " + team.get(2));
            }
        }
        else {
            System.out.println(-1);
        }
    }
}
