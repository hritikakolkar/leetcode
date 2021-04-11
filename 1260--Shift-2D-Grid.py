class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        m=len(grid)
        n=len(grid[0])
        for _ in range(k):
            grid_k=[[0]*n]*m
            for i in range(m):
                for j in range(n-1):
                    grid_k[i][j+1] = grid[i][j]
            for i in range(m-1):
                grid_k[i+1][0] = grid[i][n-1]
            grid_k[0][0] = grid[m-1][n-1]
            grid = grid_k
        return grid
        """
        """
        num_rows, num_cols = len(grid), len(grid[0])

        for _ in range(k):
            # Create a new grid to copy into.
            new_grid = [[0] * num_cols for _ in range(num_rows)]

            # Case 1: Move everything not in the last column.
            for row in range(num_rows):
                for col in range(num_cols - 1):
                    new_grid[row][col + 1] = grid[row][col]

            # Case 2: Move everything in last column, but not last row.
            for row in range(num_rows):
                 new_grid[(row+1)%num_rows][0] = grid[row][num_cols - 1]

            grid = new_grid

        return grid

        """
        
