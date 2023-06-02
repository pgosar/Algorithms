s = list(input()) + ['.']
for i, c in enumerate(s):
    if s[i-1] == c:
        for nc in 'abc':
            if s[i-1] != nc and s[i+1] != nc:
                s[i] = nc
                break
 
print(''.join(s[:len(s)-1]))
