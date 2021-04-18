"""
Runtime: 32 ms, faster than 55.42% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 14.4 MB, less than 25.90% of Python3 online submissions for Pascal's Triangle.
"""
class Solution :
    def generate(self, numRows: int) -> List[List[int]]:
        p_t = [[1],[1,1]]
        if numRows == 1 :
            return [[1]]
        elif numRows == 2 :
            return p_t
        else :
            for _ in range(numRows-2):
                temp = [1]
                for i in range(len(p_t[-1])-1) :
                    temp.append( p_t[-1][i] + p_t[-1][i+1] )
                temp.append(1)
                p_t.append(temp)
            return p_t
          
"""
Runtime: 20 ms, faster than 99.01% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 14.3 MB, less than 57.14% of Python3 online submissions for Pascal's Triangle.
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        p_t = []
        for row in range(numRows):
            tmp = [0] * (row + 1)
            for col in range(row + 1):
                if col == 0:
                    tmp[col] = 1
                elif col == row :
                    tmp[col] = 1
                else:
                    tmp[col] = p_t[row - 1][col - 1] + p_t[row - 1][col]
            p_t.append(tmp)
        return p_t
