from math import log10
class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        if string[::-1] == string:
            return True
        return False
    
    def isPalindromeNoString(self, x: int) -> bool:
	    input = x
	    new = 0
	    while x>0:
		    new = new * 10 + x%10
		    x = x//10
	    return new == input