class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        carry = 0
        while index >= 0:
            if digits[index] < 9:
                digits[index]+=1
                return digits
            else:
                digits[index] = 0
                index -= 1

        digits = [0 for _ in range(len(digits) + 1)]
        digits[0] = 1
        return digits
