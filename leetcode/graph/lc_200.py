class Solution:
    def find_one(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    return i, j

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        stack = []
        ans = 0
        if not self.find_one(grid):
            return ans
        i, j = self.find_one(grid)
        grid[i][j] = '0'
        stack.append([i, j])
        ans += 1
        move = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        while stack:
            i, j = stack.pop()
            for a, b in move:
                if 0 <= i + a < m and 0 <= j + b < n and grid[i + a][j + b] == '1':
                    grid[i + a][j + b] = '0'
                    stack.append([i + a, j + b])

            if not stack:
                if self.find_one(grid):
                    i, j = self.find_one(grid)
                    grid[i][j] = '0'
                    stack.append([i, j])
                    ans += 1

        return ans