s = input()
a,b,c=0,0,0
for i in range(len(s)):
    if s[i]=='o':
        b+=a
    elif i>0 and s[i] == 'v' and s[i-1]=='v':
        a+=1
        c+=b
print(c)
