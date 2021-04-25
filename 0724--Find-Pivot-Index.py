#Find Pivot Index
"""
Given an array of integers nums, write a method that returns the "pivot" index of this array.
We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
Example 1:
Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
 
Example 2:
Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.
 
Note:
The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].
 """
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        len_nums=len(nums)
        for i in range(0,len_nums):
            if sum(nums[:i])==sum(nums[i+1:]):
                return i
        return -1
  
# Solved after eleven months 
"""
Runtime: 152 ms, faster than 54.11% of Python3 online submissions for Find Pivot Index.
Memory Usage: 15.2 MB, less than 99.45% of Python3 online submissions for Find Pivot Index.
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for idx in range(1,len(nums)) :
            nums[idx] += nums[idx-1]
        if nums[-1]-nums[0] == 0 :
            return 0
        for idx in range(1,len(nums)-1):
            if nums[idx-1] == nums[-1] - nums[idx] :
                return idx
        if nums[-2]==0:
            return len(nums)-1
        return -1

"""
Runtime: 144 ms, faster than 86.52% of Python3 online submissions for Find Pivot Index.
Memory Usage: 15.3 MB, less than 93.46% of Python3 online submissions for Find Pivot Index.
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        cumsum = 0
        for index in range(len(nums)) :
            if cumsum == s-cumsum-nums[index]:
                return index
            cumsum += nums[index]
        return -1
       
"""
Runtime: 136 ms, faster than 98.20% of Python3 online submissions for Find Pivot Index.
Memory Usage: 15.4 MB, less than 72.86% of Python3 online submissions for Find Pivot Index.
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        prev=0
        for i,val in enumerate(nums):
            if prev==total-val:
                return i
            prev+=val
            total-=val
        return -1
                
