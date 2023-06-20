class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph, dis = defaultdict(list), [-1 for _ in range(n)]
        for f, to, price in flights:
            graph[f].append([to, price])
        dis[src], q, step = 0, deque([src]), 0
        while q and step <= k:
            sz = len(q)
            nd = list(dis)
            for _ in range(sz):
                cur = q.popleft()
                for n in graph[cur]:
                    if nd[n[0]] == -1 or nd[n[0]] > dis[cur]+n[1]:
                        nd[n[0]] = dis[cur] + n[1]
                        q.append(n[0])
            step += 1
            dis = nd
        return dis[dst]
