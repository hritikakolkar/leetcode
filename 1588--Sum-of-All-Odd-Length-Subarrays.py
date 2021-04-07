"""
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.
"""
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans=0
        for k in range(1,len(arr)+1,2):
            for i in range(len(arr)-k+1):
                ans += sum(arr[i:i+k])
        return ans
