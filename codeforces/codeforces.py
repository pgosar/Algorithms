t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=0
    i=1
    while(i<n-2):
        if arr[i]+arr[i+1]+arr[i+2]==3:
            ans+=1
            i+=2
        i+=1
    ans+=arr[0]
    print(ans)
        