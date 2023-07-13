class Solution:
    def addDigits(self, num: int) -> int:
        return num if num <= 9 else self.addDigits(sum([int(i) for i in str(num)]))
