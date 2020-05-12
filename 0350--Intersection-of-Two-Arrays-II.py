"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx=0
        jdx=0
        lst=[]
        nums1.sort()
        nums2.sort()
        while idx<len(nums1) and jdx<len(nums2):
            if nums1[idx]==nums2[jdx]:
                lst.append(nums1[idx])
                idx+=1
                jdx+=1
            elif nums1[idx]>nums2[jdx]:
                jdx+=1
            else:
                idx+=1
        return lst
