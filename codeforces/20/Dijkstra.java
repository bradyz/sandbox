import java.util.Scanner;
import java.util.HashMap;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Comparator;


class Dijkstra {
    static int node, edge;
    static int from, to, weight;
    static HashMap<Integer, HashMap<Integer, Integer> > cost = new HashMap<>();
    static HashMap<Integer, Integer> parent = new HashMap<>();
    static HashMap<Integer, Integer> distance = new HashMap<>();

    class Node {
        int val;

        public Node (int val) {
            this.val = val;
        }
    }

    void path (Integer val) {
        ArrayList<Integer> result = new ArrayList<>();

        if (val.equals(-1)) {
            System.out.println(-1);
            return;
        }

        while (val != null && val != -1) {
           result.add(val);
           val = parent.get(val); 
        }

        for (int i = result.size() - 1; i >= 0; i--) {
            System.out.print(result.get(i));
            if (i > 0)
                System.out.print(" ");
            else
                System.out.print("\n");
        }
    }

    int dijkstra () {
        Node cur;
        PriorityQueue<Node> queue = new PriorityQueue<>(new Comparator<Node>() {
            public int compare (Node lhs, Node rhs) {
                Integer lhs_distance = distance.get(lhs.val);
                Integer rhs_distance = distance.get(rhs.val);
                
                if (lhs_distance == null)
                    lhs_distance = Integer.MAX_VALUE;

                if (rhs_distance == null)
                    rhs_distance = Integer.MAX_VALUE;

                return lhs_distance - rhs_distance;
            }
        });

        distance.put(1, 0);
        queue.add(new Node(1));

        while (!queue.isEmpty()) {
            cur = queue.poll();

            if (cur.val == node)
                return cur.val;

            if (cost.get(cur.val) == null)
                continue;

            for (Integer x: cost.get(cur.val).keySet()) {
                if (distance.containsKey(x) && distance.get(x) < distance.get(cur.val) + cost.get(cur.val).get(x))
                    continue;

                distance.put(x, distance.get(cur.val) + cost.get(cur.val).get(x));
                parent.put(x, cur.val);
                queue.add(new Node(x));
            }
        }

        return -1;
    }

    public static void main (String args[]) {
        Scanner scan = new Scanner(System.in);

        node = scan.nextInt();
        edge = scan.nextInt();

        for (int i = 0; i < edge; i++) {
            from = scan.nextInt();
            to = scan.nextInt();
            weight = scan.nextInt();

            if (cost.get(from) == null)
                cost.put(from, new HashMap<>());

            if (cost.get(to) == null)
                cost.put(to, new HashMap<>());

            cost.get(from).put(to, weight);
            cost.get(to).put(from, weight);
        }

        Dijkstra d = new Dijkstra();

        d.path(d.dijkstra());
    }
}
