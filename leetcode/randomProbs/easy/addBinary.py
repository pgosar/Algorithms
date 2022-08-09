class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a=="0" and b=="0":
            return "0"
        ans = ''
        num = 0
        powerA, powerB = len(a), len(b)
        indexA, indexB = 0, 0
        while powerA or powerB:
            if powerA:
                num += int(a[indexA]) * (2**powerA)
                powerA-=1
                indexA+=1
            if powerB:
                num += int(b[indexB]) * (2**powerB)
                powerB-=1
                indexB+=1
        carry = 0
        while num > 0:
            ans += (str(num % 2))
            num //= 2
        ans = ans[1:]
        return ans[::-1]
