"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

 

Note:

The total number of elements of the given matrix will not exceed 10,000.
"""



class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix==[]: return []
        
        rowCount=len(matrix)
        colCount=len(matrix[0])
        
        ansLst=[]
        
        for row in range(rowCount):
            r=row
            c=0
            lst=[]
            while r>=0 and c<colCount:
                lst.append(matrix[r][c])
                r-=1
                c+=1
            if row%2==0:
                ansLst.extend(lst)
            else:
                ansLst.extend(list(reversed(lst)))
        for col in range(1,colCount) :
            r=rowCount-1
            c=col
            lst=[]
            while r>=0 and c<colCount:
                lst.append(matrix[r][c])
                r-=1
                c+=1
            if (rowCount-1 +col)%2==0:
                ansLst.extend(lst)
            else:
                ansLst.extend(list(reversed(lst)))
        return ansLst
