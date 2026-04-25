class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()

        def bfs(i, j):
            
            moves = ((1, 0), (0, -1), (-1, 0), (0, 1))
            queue = deque([(i, j)])

            while queue:
                x, y = queue.popleft()
                for move in moves:
                    dx, dy = move
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if (nx, ny) not in visited and grid[nx][ny] == '1':
                            queue.append((nx, ny))
                        visited.add((nx, ny))
            return visited
        

        res = 0
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j] == '1':
                    bfs(i, j)
                    res += 1
        return res
        
        

                
                    




        
        