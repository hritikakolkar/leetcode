"""
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.
"""

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique=dict()
        for num in nums:
            if num in unique:
                unique[num]+=1
            else:
                unique[num]=0
        ans=0
        for key,value in unique.items():
            if value==0:
                ans+=key
        return ans
