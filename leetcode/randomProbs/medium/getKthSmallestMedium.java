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
    public int kthSmallest(TreeNode root, int k) {
        return helper(root, new int[] {k - 1}).val;
    }
    private TreeNode helper(TreeNode root, int[] kth) {
        if (root == null) {
            return null;
        }
        TreeNode left = helper(root.left, kth);
        if (left != null) {
            return left;
        }
        if (kth[0]-- == 0) {
            return root;
        }
        return helper(root.right, kth);
    }
}
