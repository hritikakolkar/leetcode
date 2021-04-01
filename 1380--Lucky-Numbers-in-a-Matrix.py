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

#Good Solution
class Solution2:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lucky_list = list()
        min_list=list()
        max_list=list()
        m=len(matrix)
        n=len(matrix[0])
        #For collecting minimum from rows
        for i in range(m):
            min_list.append(min(matrix[i]))
        #Fro collecting maximum form columns
        for i in range(n):
            max_list.append(max([row[i] for row in matrix ]))
        
        return [lucky for lucky in min_list if lucky in max_list]
       
"""
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        T = [*zip(*matrix)]
        result = []
        for row in matrix:
            row_min = min(row)
            col_index = row.index(row_min)
            if row_min == max(T[col_index]):
                result.append(row_min)
        return result
 """
 
 """
 class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_mins = {min(r) for r in matrix}
        col_maxs = {max(c) for c in zip(*matrix)}
        return list(row_mins & col_maxs)
 """
