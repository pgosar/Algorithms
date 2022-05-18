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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> traversal = new ArrayList<>();
        helper(root, traversal);
        return traversal;
    }
    
    private void helper(TreeNode root, List<Integer> traversal) {
        if (root != null) {
            helper(root.left, traversal);
            traversal.add(root.val);
            helper(root.right, traversal);
        }
    }
}
