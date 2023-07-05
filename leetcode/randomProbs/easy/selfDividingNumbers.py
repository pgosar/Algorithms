class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [i for i in range(left, right+1) if '0' not in str(i) and all(i % int(d) == 0 for d in str(i))]
