for _ in range(int(input())):
    s = input()
    n = len(s)
    ans = float('inf')
    idx = [0, 0, 0]
    for i in range(n):
        idx[int(s[i]) - 1] = i + 1
        if (0 not in idx):
            ans = min(ans, max(idx) - min(idx) + 1)
    print(ans if ans != float('inf') else 0)
