class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        p, n, z, ans = [], [], [], set()
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        if len(z) >= 3:
            ans.add((0, 0, 0))
        if not n or not p:
            return ans
        ps, ns = set(p), set(n)

        if z:
            for i in p:
                if -1*i in ns:
                    ans.add((-1*i, 0, i))

        for i in range(len(p)):
            for j in range(i+1, len(p)):
                t = -1*(p[j] + p[i])
                if t in ns:
                    ans.add(tuple(sorted((p[j], p[i], t))))

        for i in range(len(n)):
            for j in range(i+1, len(n)):
                t = -1*(n[j] + n[i])
                if t in ps:
                    ans.add(tuple(sorted((n[j], n[i], t))))
        return ans
