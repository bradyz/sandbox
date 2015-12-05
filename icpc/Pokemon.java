/**
 * Created by naeem on 11/2/15.
 */
import java.util.*;
import java.io.*;

public class Pokemon {
    public static void main(String[] args) throws IOException {
        /* Scanner file = new Scanner(new File("pokemon.txt")); */
        Scanner file = new Scanner(System.in);

        int cases = Integer.parseInt(file.nextLine());
        for(int c = 0; c<cases; c++) {
            String[] parts = file.nextLine().split(" +");
            int numV = Integer.parseInt(parts[0]);
            int numE = Integer.parseInt(parts[1]);

            ArrayList<Node> nodes = new ArrayList<Node>();
            for(int i = 0; i < numV; i++)
                nodes.add(new Node(i, -1));
            nodes.get(0).cost = 1;

            for(int e = 0; e<numE; e++) {
                parts = file.nextLine().split(" +");
                int one = Integer.parseInt(parts[0]);
                int two = Integer.parseInt(parts[1]);
                double cost = Double.parseDouble(parts[2]);
//                System.out.println(one + " " + two + " " + cost);
                nodes.get(one).connections.put(two, cost);
                nodes.get(two).connections.put(one, cost);
            }
//            System.out.println();

            PriorityQueue<Node> q = new PriorityQueue<Node>();
            q.add(nodes.get(0));

            while(!q.isEmpty()) {
                Node n = q.poll();
                for(int i : n.connections.keySet()){
                    Node toVisit = nodes.get(i);
                    double edgeWeight = n.connections.get(i);
                    double newWeight = edgeWeight*n.cost;
                    if(newWeight > toVisit.cost) {
                        toVisit.cost = newWeight;
                        q.add(toVisit);
                    }
                }
//                System.out.println("Expanded node " + n.index);
//                for(int i = 0;i<nodes.size();i++){
//                    System.out.printf("%d: %.2f\n", i, nodes.get(i).cost);
//                }
            }

            System.out.printf("Case %d: %.2f\n", c+1, nodes.get(1).cost);
        }
    }
}

class Node implements Comparable<Node> {
    public int index;
    public double cost;
    public HashMap<Integer, Double> connections = new HashMap<Integer, Double>();

    public Node(int i, int c) {
        index = i;
        cost = c;
    }

    public int compareTo(Node other) {
        if(other.cost > cost) {
            return 1;
        }
        if(other.cost < cost) {
            return -1;
        }
        return 0;
    }
}
