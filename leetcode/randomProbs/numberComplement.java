class Solution {
    public int findComplement(int num) {
        StringBuilder binary = new StringBuilder();
        if (num == 0) return 1;
        while (num > 0) {
            binary.append(num % 2 + "");
            num /= 2;
        }
        String bin = binary.toString();
        int complement = 0;
        int index = 0;
        for(char c : bin.toCharArray()) {
            if (c == '0') {
                complement += Math.pow(2, index);
            }
            index++;
        }
        return complement;
    }
}
