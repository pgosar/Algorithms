import java.util.*;

/**
 * public class Tree {
 *   int val;
 *   Tree left;
 *   Tree right;
 * }
 */
class Solution {
    private Tree first = null;
    private Tree second = null;
    private Tree prev = null;

    public Tree solve(Tree root) {
        inorder(root);
        int temp = first.val;
        first.val = second.val;
        second.val = temp;
        return root;        
    }

    private void inorder(Tree root) {
        if (root != null) {
            inorder(root.left);
            if (first == null && (prev == null || prev.val > root.val)) {
                first = prev;
            }
            if (first != null && prev.val > root.val) {
                second = root;
            }
            prev = root;
            inorder(root.right);
        }
    }
}
