class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for word in words:
            for s in word:
                if s not in adj:
                    adj[s] = []
        n = len(words)
        i = 0
        while i < n-1:
            j = i + 1
            first = words[i]
            second = words[j]
            n1 = len(first)
            n2 = len(second)
            p=q=0
            allSame = True
            while p < n1 and q < n2:
                if first[p] != second[q]:
                    adj[first[p]].append(second[q])
                    allSame = False
                    break
                p += 1
                q += 1
            if allSame and n1 > n2: 
                return ""
            i += 1

        visit, cycle = set(), set()
        res = []
        def dfs(curr):
            if curr in cycle:
                return False
            if curr in visit:
                return True
            cycle.add(curr)
            visit.add(curr)
            for neigh in adj[curr]:
                if not dfs(neigh):
                    return False
            cycle.remove(curr)
            res.append(curr)
            return True

        for i in adj.keys():
            if i not in visit:
                if not dfs(i):
                    return ""
        return "".join(res)[::-1]

