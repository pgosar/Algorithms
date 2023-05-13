class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def gen(s, left, right, parens=[]):
            if not left and not right:
                parens.append(s)
            if left: gen(s + '(', left - 1, right, parens)
            if left < right: gen(s + ')', left, right - 1, parens)
            return parens
        return gen('', n, n)
