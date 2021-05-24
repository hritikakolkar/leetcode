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

"""
Runtime: 28 ms, faster than 94.04% of Python3 online submissions for Sum of Unique Elements.
Memory Usage: 14.2 MB, less than 41.69% of Python3 online submissions for Sum of Unique Elements.
"""
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique=dict()
        for num in nums:
            unique[num] = unique.get(num,0) + 1
        ans=0
        for key,value in unique.items():
            if value==1:
                ans+=key
        return ans
