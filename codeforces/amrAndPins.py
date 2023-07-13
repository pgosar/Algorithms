import math
r, x1, y1, x2, y2 = map(int, input().split())
dx = abs(x2 - x1)
dy = abs(y2 - y1)
print(int(math.ceil(math.sqrt(math.pow(dx / (2 * r), 2) + math.pow(dy / (2 * r), 2)))))
