/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int sumNumbers(TreeNode root) {
                return helper(root, 0);
    }

    private int helper(TreeNode root, int parent) {
        if (root == null) return 0;
        parent *= 10;
        parent += root.val;
        if (root.left == null && root.right == null) return parent;
        return helper(root.left, parent) + helper(root.right, parent);
    }
}
