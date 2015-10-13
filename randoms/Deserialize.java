import java.util.ArrayList;
import java.util.Arrays;

public class Deserialize {

    public static void printEdges (Node root) {
        for (Node child: root.children) {
            System.out.println(root.val + " " + child.val);
            printEdges(child);
        }
    }

    public static void main (String args[]) {
        Node root = new Node(1, new ArrayList<Node>(Arrays.asList(new Node(2), new Node(3))));
        root.children.get(0).children.add(new Node(4));
        root.children.get(1).children.add(new Node(5));

        printEdges(root);
    }
}

class Node {
    public int val;
    public ArrayList<Node> children;

    public Node (int val) {
        this.val = val;
        this.children = new ArrayList<Node>();
    }

    public Node (int val, ArrayList<Node> children) {
        this.val = val;
        this.children = children;
    }
}
