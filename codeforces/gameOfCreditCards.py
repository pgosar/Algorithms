n = int(input())

a = sorted(input())
b = sorted(input())
x,y=0,0

for i in range(0,n):
    if b[i]>=a[x]:
        x+=1
    if b[i]>a[y]:
        y+=1
print(n-x)
print(y)
