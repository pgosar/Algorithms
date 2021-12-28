class Solution {
    public boolean isValid(String s) {
        Stack<Character> parens = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(') parens.push(')');
            else if (c == '[') parens.push(']');
            else if (c == '{') parens.push('}');
            else if (stack.isEmpty() || parens.pop() != c) return false;
        }
        return parens.isEmpty();
}
