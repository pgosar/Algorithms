class Solution {
    public String toLowerCase(String s) {
        StringBuilder lower = new StringBuilder();
        for (char c : s.toCharArray()) {
            if ('A' <= c && c <= 'Z') {
                lower.append((char) (c + 32));
            } else {
                lower.append((char) c);
            }
        }
        return lower.toString();
    }
}
