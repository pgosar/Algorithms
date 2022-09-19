cols = int(input())
cubes = [int(i) for i in input().split()]
cubes.sort()

for i in range(cols):
    print(cubes[i])
