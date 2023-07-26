import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    s = s.replace("twone", "tw#ne")
    s = s.replace("one", "o#e")
    s = s.replace("two", "t#o")
    res = []
    for i, item in enumerate(s):
        if item == '#':
            res.append(i+1)
    print(len(res))
    print(' '.join(map(str, res)))
