"""
Runtime: 24 ms, faster than 98.41% of Python3 online submissions for Check if Array Is Sorted and Rotated.
Memory Usage: 14 MB, less than 98.82% of Python3 online submissions for Check if Array Is Sorted and Rotated.
"""
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        for idx in range(len(nums)) :
            if nums[idx-1] > nums[idx] :
                count += 1
        return count <= 1
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        for idx in range(len(nums)) :
            if nums[idx-1] > nums[idx] :
                count += 1
                if count > 1 :
                    return False
        return True 
