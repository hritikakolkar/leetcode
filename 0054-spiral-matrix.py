"""
Spiral matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix==[]:
            return []
        top=0
        right=len(matrix[0])-1
        down=len(matrix)-1
        left=0
        direction=0
        #if direction = 0 move left to right
        #if direction = 1 move top to bottom
        #if direction = 2 move right to left
        #if direction = 3 move bottom ot top
        ans_lst=[]
        while (top<=down and left<=right):
            if direction==0:
                for mov in range(left,right+1):
                    ans_lst.append(matrix[top][mov])
                top+=1
            if direction==1:
                for mov in range(top,down+1):
                    ans_lst.append(matrix[mov][right])
                right-=1
            if direction==2:
                for mov in reversed(range(left,right+1)):
                    ans_lst.append(matrix[down][mov])
                down-=1
            if direction==3:
                for mov in reversed(range(top,down+1)):
                    ans_lst.append(matrix[mov][left])
                left+=1
            direction=(direction+1)%4
        return ans_lst
