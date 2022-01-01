import java.util.*;

/**
 * public class Tree {
 *   int val;
 *   Tree left;
 *   Tree right;
 * }
 */
class Solution {
    public boolean solve(Tree root) {
        StringBuilder left = new StringBuilder();
        inOrderLeft(root, left);
        StringBuilder right = new StringBuilder();
        inOrderRight(root, right);
        return left.toString().equals(right.toString());
    }

    private void inOrderLeft(Tree root, StringBuilder sb) {
        if (root != null) {
            inOrderLeft(root.left, sb);
            sb.append(root.val);
            inOrderLeft(root.right, sb);
        }
    }

    private void inOrderRight(Tree root, StringBuilder sb) {
        if (root != null) {
            inOrderRight(root.right, sb);
            sb.append(root.val);
            inOrderRight(root.left, sb);
        }
    }
}
