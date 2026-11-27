class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid), len(grid[0])
        if grid[rows - 1][cols - 1] == 1 or grid[0][0] == 1:
            return -1
        length = 0
        queue = deque()
        visited = set()
        queue.append((0, 0))
        visited.add((0, 0))

        while len(queue):
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length
                
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if min(nr, nc) < 0 or nr == rows or nc == cols or (nr, nc) in visited or grid[nr][nc] == 1:
                        continue
                    queue.append((nr, nc))
                    visited.add((nr, nc))
            length += 1
        return -1       
