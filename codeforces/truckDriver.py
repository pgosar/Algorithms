k = int(input())
weights = [int(x) for x in input().split()]
weights.sort()
weightsNew = weights[::-1]
print(weightsNew[k - 1])
