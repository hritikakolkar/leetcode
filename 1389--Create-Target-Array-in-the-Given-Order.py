"""
Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.
"""

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        len_nums=len(nums)
        target=[]
        def push(lst,index,data):
            return lst[:index]+[data]+lst[index:]
        for i in range(len_nums):
            target=push(target,index[i],nums[i])
        return target
        
class Solution1:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target=list()
        for i in range(len(nums)) :
            target.insert(index[i],nums[i])
        return target

class Solution2:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        arr = []
        for n,i in zip(nums,index): 
            arr[i:i] = [n]
        return arr
