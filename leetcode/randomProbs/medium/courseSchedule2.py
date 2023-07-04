class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = {i:set() for i in range(numCourses)}
        graph = collections.defaultdict(set)
        for i,j in prerequisites:
            pre[i].add(j)
            graph[j].add(i)
        q = collections.deque([])
        for k, v in pre.items():
            if len(v) == 0:
                q.append(k)
        taken = []
        while q:
            course = q.popleft()
            taken.append(course)
            if len(taken) == numCourses:
                return taken
            for i in graph[course]:
                pre[i].remove(course)
                if not pre[i]:
                    q.append(i)
        return []
