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
        int[] count = new int[] {Integer.MIN_VALUE};
        helper(root, count);
        return count[0];
    }

    public int helper(Tree root, int[] count) {
        if (root == null) return 0;
        int left = helper(root.left, count);
        int right = helper(root.right, count);
        count[0] = Math.max(count[0], root.val + left + right);
        return Math.max(0, root.val + Math.max(left, right));
    }
}
