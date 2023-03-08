"""
You are given a 0-indexed integer array nums. For each index i (1 <= i <= nums.length - 2) the beauty of nums[i] equals:
  - 2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.
  - 1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.
  - 0, if none of the previous conditions holds.
Return the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2.
"""


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        ans = 0
        max_j= nums[0]
        min_k = float("inf")
        minimum = []
        length = len(nums)
        for i in range(length-1,-1,-1):
            min_k = min(nums[i],min_k)
            minimum.append(min_k)
        minimum = minimum[::-1]
        for i in range(1,length-1):
            if max_j< nums[i] < minimum[i+1]:
                ans += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                ans += 1
            max_j = max(nums[i],max_j)
        return ans
