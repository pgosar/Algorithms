import java.util.*;

/**
 * public class Tree {
 *   int val;
 *   Tree left;
 *   Tree right;
 * }
 */
class BSTIterator {
    Stack<Tree> stack;
    Tree curr;
    public BSTIterator(Tree root) {
        stack = new Stack<Tree>();
        curr = root;
    }

    public int next() {
        while (curr != null) {
            stack.push(curr);
            curr = curr.left;
        }
        Tree temp = stack.pop();
        curr = temp.right;
        return temp.val;
    }

    public boolean hasnext() {
        return !stack.isEmpty() || curr != null;

    }
}
