class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        parent = [x for x in range(n)]
        def find(x):
            if parent[x] != x:
                return find(parent[x])
            else:
                return x

        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return False
            parent[y] = x
            return True

        for x,y in edges:
            if not union(x,y):
                return False

        return True

        # if len(edges) != n - 1:
        #     return False  # Too few => disconnected, too many => cycle

        # # Step 2: Initialize parent array where each node is its own parent
        # parent = [i for i in range(n)]  # parent[i] = parent of node i

        # # Step 3: Define the find function with path compression
        # def find(x):
        #     # If x is not its own parent, recursively find its root
        #     if parent[x] != x:
        #         parent[x] = find(parent[x])  # Path compression
        #     return parent[x]

        # # Step 4: Define the union function to merge two sets
        # def union(x, y):
        #     rootX = find(x)  # Find root of x
        #     rootY = find(y)  # Find root of y

        #     if rootX == rootY:
        #         return False  # x and y are already connected => cycle
        #     parent[rootX] = rootY  # Merge sets by connecting roots
        #     return True

        # # Step 5: Process all edges
        # for u, v in edges:
        #     if not union(u, v):
        #         return False  # If union fails, a cycle exists

        # # Step 6: No cycles, and exactly n - 1 edges => valid tree
        # return True