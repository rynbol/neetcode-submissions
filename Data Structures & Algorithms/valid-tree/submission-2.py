class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        res = []
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            res.append(node)
            for neigh in graph[node]:
                if neigh == parent:
                    continue
                if not dfs(neigh, node):
                    return False
            return True

        if not dfs(0, -1):
            return False
        return len(res) == n