#counting elements
"""
Given an integer array arr, count element x such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.
"""
class Solution:
    def countElements(self, arr: List[int]) -> int:
        count=0
        for i in arr:
            if i+1 in arr:
                count+=1
        return count
