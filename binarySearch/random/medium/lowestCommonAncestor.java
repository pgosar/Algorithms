import java.util.*;

/**
 * public class Tree {
 *   int val;
 *   Tree left;
 *   Tree right;
 * }
 */
class Solution {
    public int solve(Tree root, int a, int b) {
        Tree ans = helper(root, a, b);
        return ans.val;
    }

    public Tree helper(Tree node, int a, int b) {
        if (node == null || node.val == a 
            || node.val == b) return node;
        Tree left = helper(node.left, a, b);
        Tree right = helper(node.right, a, b);
        if (left != null && right != null) return node;
        else if (left != null && right == null) return left;
        else return right;
    }
}
