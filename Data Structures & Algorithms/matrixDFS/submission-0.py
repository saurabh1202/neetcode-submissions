class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        def countPaths1(grid:List[List[int]], r:int, c:int, visit:set) -> int:
            
            rows , cols = len(grid), len(grid[0])
            if min(r, c) < 0 or r == rows or c == cols or (r, c) in visit or grid[r][c] == 1:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1
            
            visit.add((r, c))
            count = 0
            count += countPaths1(grid, r + 1, c, visit)
            count += countPaths1(grid, r - 1, c, visit)
            count += countPaths1(grid, r, c + 1, visit)
            count += countPaths1(grid, r, c - 1, visit)

            visit.remove((r, c))

            return count
        visit = set()
        return countPaths1(grid, 0, 0, visit)
        