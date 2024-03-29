"""
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].
 
"""
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)) :
            image[i]=list(reversed(image[i]))
            for j in range(len(image[i])):
                image[i][j]=1-image[i][j]
        return image

#Great solution fro leetcode
"""
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in A:
            l = 0
            r = len(i) -1
            while(l<=r):
                i[r], i[l] = 1-i[l],1-i[r]
                l+=1
                r-=1
        return A
 """
#old Solution
"""
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)) :
            image[i]=list(reversed(image[i]))
            for j in range(len(image[i])):
                if image[i][j]==0:
                    image[i][j]=1
                else:
                    image[i][j]=0
        return image
"""
