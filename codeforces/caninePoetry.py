for _ in range(int(input())):
    s = input()
    ans = 0
    replacements = [False for _ in range(len(s))]
    for i in range(1, len(s)):
        if (i > 1 and s[i] == s[i-2] and not replacements[i-2]) or (s[i] == s[i-1] and not replacements[i-1]):
            replacements[i] = True
            ans += 1
    print(ans)
