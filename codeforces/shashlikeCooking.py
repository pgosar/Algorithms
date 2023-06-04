import sys
input = sys.stdin.readline

n,k=map(int,input().split())
ans=n//(2*k+1)
if n%(2*k+1)!=0:
    ans+=1
print(ans)
i=k+1
x=i+(2*k+1)*(ans-1)
if x>n:
    i-=x-n
while i<=n:
    print(i, end=' ')
    i+=2*k+1
