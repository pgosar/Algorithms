import java.util.*;

/**
 * public class Tree {
 *   int val;
 *   Tree left;
 *   Tree right;
 * }
 */
class Solution {
    public int solve(Tree root, int k) {
        return helper(root, new int[] {k}).val;
    }

    private Tree helper(Tree root, int[] k) {
        if (root == null) return null;
        Tree left = helper(root.left, k);
        if (left != null) return left;
        if (k[0]-- == 0) return root;
        return helper(root.right, k);
    }
}
