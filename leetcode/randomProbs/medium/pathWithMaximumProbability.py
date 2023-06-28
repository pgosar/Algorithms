class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i, c in enumerate(edges):
            graph[c[0]].append((c[1], succProb[i]))
            graph[c[1]].append((c[0], succProb[i]))

        heap = [(-1, start)]
        seen = set()
        print(graph)
        while heap:
            prob, cur = heappop(heap)
            seen.add(cur)
            if cur == end:
                return -prob
            for n, p in graph[cur]:
                if n not in seen:
                    tmp = p * prob
                    heappush(heap, (tmp, n))
        return 0
