n = int(input())
denoms = [100, 20, 10, 5, 1]
index = 0
total = 0
while n > 0 and index < len(denoms):
    if n >= denoms[index]:
        total += 1
        n -= denoms[index]
    else:
        index += 1
        
print(total)
        