"""
0169--Majority-Element.py
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in list(set(nums)):
            if nums.count(i)>len(nums)/2:
                return i
