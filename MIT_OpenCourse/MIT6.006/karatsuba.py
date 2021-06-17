#this is an algorithm to make multiplication faster using divide and conquer
#Instead of O(n^2) we can get O(n^log3) or O(n^1.59)
#this approach uses bitwise operators


lookuptable = { #dictionary to handle negatives and stuff so i dont need to use the *
  (-1,-1): 1, (-1,0): 0, (-1, 1): -1,
  (0,-1): 0, (0,0):0, (0,1): 0,
  (1,-1): -1, (1,0): 0, (1,1): 1}

def karatsuba(x,y):
  num = max(x.bit_length(), y.bit_length())

  if num < 2:
    return lookuptable[(x,y)]

  num = num >> 1

  b = x >> num
  a = x - (b << num) #this is a left shift
  d = y >> num #this is a right shift
  c = y - (d << num)

  ac = karatsuba(a, c)
  bd = karatsuba(b, d)
  abcd = karatsuba(a+b, c+d)

  return ac + ((abcd - ac - bd) << num) + (bd << (num << 1))

print(karatsuba(23,24))
print(karatsuba(3,-4))

def karatsubaOneLine(x,y):
    if max(x.bit_length(), y.bit_length()) < 2:
        return lookuptable[(x,y)]
    #i tried doing this for fun and it didnt work, I'm not gonna bug fix it. i would need to write a new method to do the recursion
    return (karatsuba(x - ((x >> (max(x.bit_length(), y.bit_length()) >> 1)) << (max(x.bit_length(), y.bit_length()) >> 1)), y- ((y >> (max(x.bit_length(), y.bit_length()) >> 1)) << (max(x.bit_length(), y.bit_length()) >> 1)))+ ((karatsuba(x-((x >> (max(x.bit_length(), y.bit_length()) >> 1)) << (max(x.bit_length(), y.bit_length()) >> 1)) + x >> (max(x.bit_length(), y.bit_length()) >> 1), y - ((y >> (max(x.bit_length(), y.bit_length()) >> 1)) << (max(x.bit_length(), y.bit_length()) >> 1)) + y >>(max(x.bit_length(), y.bit_length()) >> 1))- karatsuba(x - ((x >> (max(x.bit_length(), y.bit_length()) >> 1) < 2) << (max(x.bit_length(), y.bit_length()) >> 1) < 2), y- ((y >> (max(x.bit_length(), y.bit_length()) >> 1) < 2) << (max(x.bit_length(), y.bit_length()) >> 1) < 2)) - karatsuba(x >> (max(x.bit_length(), y.bit_length()) >> 1), y >> (max(x.bit_length(), y.bit_length()) >> 1))) << (max(x.bit_length(), y.bit_length()) >> 1)) + (karatsuba(x >> (max(x.bit_length(), y.bit_length()) >> 1), y >> (max(x.bit_length(), y.bit_length()) >> 1)) << ((max(x.bit_length(), y.bit_length()) >> 1) << 1)))
  
print(karatsubaOneLine(23,24))