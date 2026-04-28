class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        q = deque([(0, 0, 0, 0)])
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        n = len(grid)
        m = len(grid[0])

        while q:
            x, y, px, py = q.popleft()
            value = grid[y][x]
            if (x, y) not in visited:
                visited.add((x, y))
                for dx, dy in moves:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[ny][nx] == value:
                            if (nx, ny) in visited and (nx, ny) != (px, py):
                                return True
                            if (nx, ny) not in visited:
                                q.appendleft((nx, ny, x, y))
                        else:
                            if (nx, ny) not in visited:
                                q.append((nx, ny, nx, ny))

        return False