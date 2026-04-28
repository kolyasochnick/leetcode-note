class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # 1 - 3
        n = len(grid)
        m = len(grid[0])

        stack = [(0, 0)]
        visited = set()
        route = {
                1: [(1, 0), (-1, 0)],
                2: [(0, 1), (0, -1)], 
                3: [(0, 1), (-1, 0)], 
                4: [(0, 1), (1, 0)],
                5: [(-1, 0), (0, -1)],
                6: [(0, -1), (1, 0)]
                }
        while stack:
            x, y = stack.pop()

            if y == n-1 and x == m-1:
                return True
            if (x, y) not in visited:
                visited.add((x, y))
                for i in range(2):
                    dx, dy = route[grid[y][x]][i]
                    nx = dx + x
                    ny = dy + y
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                        for j in range(2):
                            bx, by = route[grid[ny][nx]][j]

                            if (nx + bx) == x and (ny + by) == y:
                                stack.append((nx, ny))
            
        return x == m-1 and y == n-1
            




        