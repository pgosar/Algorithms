I=lambda:map(int,input().split())
n,q,k=I()
a=list(I())
for _ in range(q):l,r=I();print(k+a[r-1]-a[l-1]-2*(r-l)-1)
