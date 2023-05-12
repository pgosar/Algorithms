import sys
input = sys.stdin.readline

n = int(input())
angles = []
for _ in range(n):
    angles.append(int(input()))

def helper(angles, total, index):
    if index == len(angles):
        return total % 360 == 0
    return helper(angles, total + angles[index], index + 1) or helper(angles, total - angles[index], index + 1)

print("YES" if helper(angles, 0, 0) else "NO")
