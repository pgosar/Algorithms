for _ in range(int(input())):
    s = input()
    tmp = []
    ans = 0
    for i in s:
        if i not in tmp:
            tmp.append(i)
        else:
            ans += len(tmp) - 1
            tmp = []
    print(ans+len(tmp))