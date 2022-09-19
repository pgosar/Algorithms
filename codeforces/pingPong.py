path = []
n = int(input())
for it in range(0, n):
    data = list(map(int, input().split()))
    if data[0] == 1:
        path.append(data[1:])
    else:
        vis = [False] * (len(path) + 1)
        q = [data[1] - 1]
        while len(q):
            p = q[0]
            del q[0]
            for i, v in enumerate(path):
                if (v[0] < path[p][0] < v[1] or v[0] < path[p][1] < v[1]) and not vis[i]:
                    vis[i] = True
                    q.append(i)
        print('YES' if vis[data[2] - 1] else 'NO')
