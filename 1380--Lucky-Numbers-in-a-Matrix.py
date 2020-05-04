"""
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 
"""
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        matrix_t=list(zip(*matrix))
        print(matrix_t)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if min(matrix[i])==matrix[i][j] and max(matrix_t[j])==matrix[i][j]:
                    ans.append(matrix[i][j])
        return ans
