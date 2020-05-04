"""
Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
"""
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        def check(number,arr,d):
            for i in arr:
                if abs(number-i)<=d:
                    return False
            return True
        count=0
        for i in arr1:
            if check(i,arr2,d):
                count+=1
        return count
