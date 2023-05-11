import bisect

n = int(input())
    
arr = sorted(list(map(int,input().split())))
q = int(input())

for i in range(q):
    print(bisect.bisect(arr, int(input())))