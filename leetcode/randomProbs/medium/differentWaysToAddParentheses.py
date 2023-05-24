class Solution:
    def helper(self, expression, m):
        n = []
        if expression in m:
            return m[expression]
        if expression.isdigit():
            m[expression] = int(expression)
            n.append(int(expression))
            return n
        for i, c in enumerate(expression):
            if c in '+-*':
                 l = self.diffWaysToCompute(expression[:i])
                 r = self.diffWaysToCompute(expression[i+1:])
                 for j in l:
                     for k in r:
                         n.append(eval(str(j)+expression[i]+str(k)))
        m[expression] = n
        return n
    def diffWaysToCompute(self, expression: str) -> List[int]:
        mem = {}
        return self.helper(expression, mem)
