#4. Median of Two Sorted Arrays
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst=sorted(nums1+nums2)
        len_lst=len(lst)
        if len_lst%2==0:
            return float((lst[len_lst//2]+lst[len_lst//2-1])/2)
        else:
            return float(lst[len_lst//2])
