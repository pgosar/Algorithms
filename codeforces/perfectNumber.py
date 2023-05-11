k = int(input()) 
start = 10
while k != 0:
    sum = 0
    start += 9
    for i in str(start):
        sum += int(i)
    if sum == 10:
        k -= 1
print(start)
