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
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> paths = new ArrayList<String>();
        if (root != null) helper(root, new StringBuilder(), paths);
        return paths;
    }

    public void helper(TreeNode root, StringBuilder path, List<String> paths) {
        if (root.left == null && root.right == null) {
            paths.add(path.append(root.val).toString());
        }
        if (root.left != null) {
            String prev = path.toString();
            helper(root.left, path.append(root.val).append("->"), paths);
            path = new StringBuilder(prev);
        }
        if (root.right != null) {
            helper(root.right, path.append(root.val).append("->"), paths);
        }
    }
}
