class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True

# Solution for less memeory but more time taken from leetcode
class Solution1:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        h = len(matrix)
        w = len(matrix[0])
        def valid(r, c):
            target = matrix[r][c]
            r += 1
            c += 1
            while r < h and c < w:
                if matrix[r][c] != target:
                    return False
                r += 1
                c += 1
            return True
        for c in range(w):
            if not valid(0, c):
                return False
        for r in range(1, h):
            if not valid(r, 0):
                return False
        return True
