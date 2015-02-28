import java.util.Scanner;
import java.util.Stack;

public class ExpressionTree<T> extends BinaryTree<T> {

    public static ExpressionTree<Character> makeExpressionTree(String postfix) {
        Stack<BinaryNode<Character>> etree = new Stack<BinaryNode<Character>>();
        BinaryTree<Character> tmptree = new BinaryTree<Character>();
        /* System.out.println(postfix); */
        for(int i = 0; i < postfix.length(); i++) {
            char current = postfix.charAt(i);
            if (isOperator(current)) {
                BinaryNode<Character> right = etree.pop();
                BinaryNode<Character> left = etree.pop();
                tmptree.root = new BinaryNode<Character>(current, left, right);
                /* System.out.println(tmptree.toString()); */
                etree.push(tmptree.root);
            }
            else {
                etree.push(new BinaryNode<Character>(current, null, null));
            }
        }
        
        System.out.println(tmptree.toString());
        return null;
    }

    private static boolean isOperator(char current) {
        return (current == '+') || (current == '-') || (current == '*') ||
            (current == '/');

    }

    public static void main (String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a postfix arithmetic expression: ");
        String postfix = input.nextLine();
        postfix = postfix.replaceAll("\\s+","");
        ExpressionTree.makeExpressionTree(postfix);
    }
}
