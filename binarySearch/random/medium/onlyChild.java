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
        if (root == null) return 0;
        int count = 0;
        if ( (root.right == null && root.left != null) || 
            (root.left == null && root.right != null) ) {
            count++;
        }
        return count + solve(root.left) + solve(root.right);
    }
}
