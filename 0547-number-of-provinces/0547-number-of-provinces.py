class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        used = [False] * n
        res = 0

        for i in range(n):
            if used[i]:
                continue
            
            res += 1
            stack = [i]

            while stack:
                v = stack.pop()

                if used[v]:
                    continue
                
                used[v] = True

                for u in range(n - 1, -1, -1):
                    if isConnected[v][u] == 1 and not used[u]:
                        stack.append(u)
        return res