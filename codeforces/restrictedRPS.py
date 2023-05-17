import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a, b, c = map(int, input().split())
    st = input()
    r, p, s = st.count('R'), st.count('P'), st.count('S')
    r, p, s = min(r, b), min(p, c), min(s, a)
    if 2 * (r + p + s) >= n:
        print('YES')
        print(st.replace('R', 'p', r).replace('P', 's', p)
              .replace('S', 'r', s).replace(R', 'x')
              .replace('S', 'x').replace('P', 'x')
              .replace('x', 'r', a - s).replace('x', 'p', b - r)
              .replace('x', 's', c - p).upper())
    else:
        print('NO')
