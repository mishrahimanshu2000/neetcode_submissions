class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        indegree = [0] * numCourses 
        res = []
        for u,v in prerequisites:
            g[v].append(u)
            indegree[u] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        taken = len(q)
        while q:
            u = q.popleft()
            res.append(u)
            for v in g[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
                    taken += 1
        if taken == numCourses:
            return res
        return []