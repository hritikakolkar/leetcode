"""
Runtime: 1456 ms, faster than 5.18% of Python3 online submissions for Maximum Average Subarray I.
Memory Usage: 26.4 MB, less than 12.54% of Python3 online submissions for Maximum Average Subarray I.
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        ans = nums[k-1]/k
        for i in range(1,len(nums)-k+1) :
            ans = max((-nums[i-1]+nums[i+k-1])/k,ans)
        return ans
"""
Runtime: 1192 ms, faster than 22.58% of Python3 online submissions for Maximum Average Subarray I.
Memory Usage: 26.2 MB, less than 26.33% of Python3 online submissions for Maximum Average Subarray I.
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum = summation = sum(nums[:k])
        for idx in range(k,len(nums)):
            summation += nums[idx] - nums[idx-k]
            maximum = max(summation,maximum)
        return maximum/k
