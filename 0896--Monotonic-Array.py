"""
Runtime: 460 ms, faster than 77.31% of Python3 online submissions for Monotonic Array.
Memory Usage: 20.5 MB, less than 83.71% of Python3 online submissions for Monotonic Array
"""
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc, dec = True, True
        temp = A[0]
        for num in A[1:]:
            if num < temp: inc = False
            if num > temp: dec = False
            temp = num
        return inc or dec

