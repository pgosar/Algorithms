class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def solve(key, k, ans):
            j = 0
            for i in range(len(key)):
                k -= key[i] != ans
                if k < 0:
                    k += key[j] != ans
                    j+=1
            return len(key) - j
        return max(solve(answerKey, k, 'T'), solve(answerKey, k, 'F'))
