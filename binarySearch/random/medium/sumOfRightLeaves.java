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
        return helper(root, false);
    }

    private int helper(Tree root, boolean isRight) {
        if (root == null) return 0;
        if (root.left == null && root.right == null && isRight) {
            return root.val;
        }
        return helper(root.left, false) + helper(root.right, true);
    }
}
