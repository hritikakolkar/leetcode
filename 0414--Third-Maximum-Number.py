"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=set(nums)
        if len(nums)<3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)
