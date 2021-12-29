import java.util.*;

/**
 * public class Tree {
 *   int val;
 *   Tree left;
 *   Tree right;
 * }
 */
class Solution {
    public int solve(Tree root) {
        return helper(root, 0);
    }

    private int helper(Tree root, int val) {
        if (root == null) return 0;
        val *= 10;
        val += root.val;
        if (root.left == null && root.right == null) return val;
        return helper(root.left, val) + helper(root.right, val);
    }
}
