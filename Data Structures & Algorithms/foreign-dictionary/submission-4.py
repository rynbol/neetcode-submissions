class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        edges = {}

        for word in words:
            for i in word:
                if i not in edges: 
                    edges[i] = []
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
                    allSame = False
                    break
            if n1 > n2 and allSame:
                return ""
            i += 1
            
        visit, cycle = set(), set()
        res = []
        def dfs(curr):
            if curr in cycle:
                return False
            if curr in visit:
                return True
            visit.add(curr)
            cycle.add(curr)
            for neigh in edges[curr]:
                if not dfs(neigh):
                    return False
            res.append(curr)
            cycle.remove(curr)
            return True

        for edge in edges.keys():
            if edge not in visit:
                if not dfs(edge):
                    return ""

        return "".join(res)[::-1]
