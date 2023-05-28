import sys
input = sys.stdin.readline

for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    d=dict(zip(a,b))
    ans=0
    while d:
        ans+=1
        k, v = d.popitem()
        while k != v:
            v = d.pop(v)
    print(pow(2, ans, 10**9+7))
