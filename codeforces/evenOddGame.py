import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    alice = 0
    bob = 0
    for i, c in enumerate(a):
        if i % 2 == 0:
            if c % 2 == 0:
                alice += c
        else:
            if c % 2 != 0:
                bob += c
    if alice > bob:
        print("Alice")
    elif bob > alice:
        print("Bob")
    else:
        print("Tie")
