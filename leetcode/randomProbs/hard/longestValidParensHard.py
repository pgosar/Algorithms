import collections

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        deque = collections.deque([-1])
        longest = 0
        for i, c in enumerate(s):
            if c == '(':
                deque.append(i)
            else:
                deque.pop()
                if not deque:
                    deque.append(i)
                longest = max(longest, i-deque[-1])
        return longest
