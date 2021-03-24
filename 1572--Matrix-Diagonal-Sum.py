
"""
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
"""

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        ans=0
        for i in range(n):
            for j in range(n):
                if i==j or i+j==n-1:
                    ans+=mat[i][j]
        return ans
#fast solution from leetcode
"""
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        length = len(mat)
        
        if length % 2 != 0:
            mid = length // 2
            result -= mat[mid][mid]
        for i in range(length):
            result += mat[i][i]
            result += mat[i][-1 - i]
        return result
 """
