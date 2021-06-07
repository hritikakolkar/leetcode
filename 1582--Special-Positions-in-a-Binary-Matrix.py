class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m=len(mat)
        n=len(mat[0])
        special=0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if mat[i].count(1)==1 and [mat[i][j] for i in range(m) ].count(1)==1:
                        special += 1
        return special

# good soltuion copied
class Solution1:
    def numSpecial(self, mat: List[List[int]]) -> int:
        return sum([1 if (mat[row].count(1)==1) else 0 for row in [col.index(1)  for col in zip(*mat) if (col.count(1)==1)]])
