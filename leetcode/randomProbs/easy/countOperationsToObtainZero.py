class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        return 1 + self.countOperations(max(num1, num2)-min(num1, num2), min(num1, num2)) if num1*num2 != 0 else 0
