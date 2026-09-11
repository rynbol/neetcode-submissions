class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        edges = {}
        indegree = {}

        for word in words:
            for i in word:
                if i not in edges: 
                    edges[i] = []
                    indegree[i] = 0
        i = 0
        while i < n-1:
            j = i + 1
            first = words[i]
            second = words[j]
            n1, n2= len(first), len(second)
            p, q = 0, 0
            allSame = True
            while p < n1 and q < n2:
                if first[p] == second[q]:
                    p += 1
                    q += 1
                elif first[p] != second[q]:
                    edges[first[p]].append(second[q])
                    indegree[second[q]] = indegree.get(second[q], 0) + 1
                    allSame = False
                    break
            if n1 > n2 and allSame:
                return ""
            i += 1

        q = deque()
        for key, val in indegree.items():
            if val == 0:
                q.append(key)
        res = []
        while q:
            popped = q.popleft()
            res.append(popped)
            for neigh in edges[popped]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
            
        return ''.join(res) if len(res) == len(edges) else ""