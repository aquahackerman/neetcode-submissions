from collections import deque

class Solution:
    def swimInWater(self, grid):
        n = len(grid)

        t = grid[0][0]
        visited = set([(0, 0)])

        while True:
            q = deque([(0, 0)])
            reachable = set([(0, 0)])

            min_blocked = float("inf")

            while q:
                r, c = q.popleft()

                if (r, c) == (n - 1, n - 1):
                    return t

                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < n and 0 <= nc < n):
                        continue

                    if (nr, nc) in reachable:
                        continue

                    if grid[nr][nc] <= t:
                        reachable.add((nr, nc))
                        q.append((nr, nc))
                    else:
                        min_blocked = min(min_blocked, grid[nr][nc])

            t = min_blocked