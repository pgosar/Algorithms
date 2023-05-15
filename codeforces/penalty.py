t = int(input())
 
for case in range(t):
 
    s = input()
    n = len(s)
 
    count_a = 0
    count_b = 0
    for i, x in enumerate(s):
        if x == '?' or (i%2 == 0 and x == '0') or (i%2 == 1 and x == '1'):
            count_a += 1
 
        if x == '?' or (i%2 == 0 and x == '1') or (i%2 == 1 and x == '0'):
            count_b += 1
 
        if 2 * count_a > n or 2 * count_b > n:
            print(i + 1)
            break
 
    else:
        print(n)
