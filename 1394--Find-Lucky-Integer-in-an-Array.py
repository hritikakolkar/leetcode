"""
1394. Find Lucky Integer in an Array

Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.

Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
"""
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky=-1
        for i in arr:
            if i==arr.count(i):
                if i>lucky:
                    lucky=i
        return lucky 
