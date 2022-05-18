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
    public int maxPathSum(TreeNode root) {
        int[] maxValue = new int[] {Integer.MIN_VALUE};
        helper(root, maxValue);
        return maxValue[0];
    }
    
    public int helper(TreeNode root, int[] maxValue) {
        if (root == null) return 0;
        int max = Integer.MIN_VALUE;
        int left = Math.max(helper(root.left, maxValue), 0);
        int right = Math.max(helper(root.right, maxValue), 0);
        max = Math.max(max, left + right + root.val);
        maxValue[0] = Math.max(max, maxValue[0]);
        return root.val + Math.max(left, right);
    }
}
