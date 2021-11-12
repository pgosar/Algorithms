class Solution {
    public int solve(Tree root) {
        if (root == null) {
            return 0;
        }
        int left = left(root);
        int right = right(root);
        if (left == right) {
            return (1 << left) - 1;
        } else {
            return 1 + solve(root.left) + solve(root.right);
        }
    }
    
    private int left(Tree root) {
        int count = 0;
        while (root != null) {
            count++;
            root = root.left;
        }
        return count;
    }

    private int right(Tree root) {
        int count = 0;
        while (root != null) {
            count++;
            root = root.right;
        }
        return count;
    }
}
