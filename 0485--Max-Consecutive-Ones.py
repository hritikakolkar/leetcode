"""
Runtime: 368 ms, faster than 30.28% of Python3 online submissions for Max Consecutive Ones.
Memory Usage: 14.5 MB, less than 18.47% of Python3 online submissions for Max Consecutive Ones.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        max_ones = 0
        for num in nums:
            if num :
                ones += 1
                max_ones = max(max_ones, ones)
            else:
                ones = 0
        return max_ones
