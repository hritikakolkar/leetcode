"""
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.
"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n=0
        for idx in range(len(nums)):
            for jdx in range(idx,len(nums)):
                if (nums[idx]==nums[jdx]) and idx<jdx :
                    n=n+1
        return n
                  
#8ms on leetcode code copied
"""
class Solution:
 def numIdenticalPairs(self, nums):
  f={}
  ans=0
  for num in nums:
   if not num in f:
    f[num]=0
   f[num]+=1
  for num in f:
   n=f[num]
   ans+=(n*(n-1)//2)
  return ans
  """
