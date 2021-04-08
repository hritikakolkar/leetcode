class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        min_nums=min(nums)
        if min_nums<1:
            return -min_nums +1
        else:
            return 1
       
class Solution1:
    def minStartValue(self, nums: List[int]) -> int:
        min_nums=nums[0]
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
            min_nums=min(min_nums,nums[i])
        if min_nums<1:
            return 1-min_nums
        else:
            return 1

class Solution2:
    def minStartValue(self, nums: List[int]) -> int:
        min_nums=nums[0]
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
            min_nums=min(min_nums,nums[i])
        return max(1,1-min_nums)       
          
