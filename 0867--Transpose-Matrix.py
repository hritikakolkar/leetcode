class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))

class Solution1:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return zip(*matrix)

class Solution2:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        t_matrix=list()
        for j in range(len(matrix[0])):
                t_matrix.append([matrix[i][j] for i in range(len(matrix))])
        return t_matrix
