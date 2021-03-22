"""
1365. How Many Numbers Are Smaller Than the Current Number
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=[]
        for i in nums:
            count_num=0
            for j in nums:
                if j<i:
                    count_num+=1
            count.append(count_num)
        return count
    
#After Solving after 11 months

"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""
#very bad caode hritik
"""
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans_lst=list()
        for i in range(len(nums)):
            valid_j=0
            for j in range(len(nums)):
                if j!=i and nums[j]<nums[i]:
                    valid_j+=1
            ans_lst.append(valid_j)
        return ans_lst
"""
# Leetcode copied soltuion 48ms
"""
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        mapping = {}
        for i, n in enumerate(sorted((nums))):
            if n not in mapping:
                mapping[n] = i
        return [mapping[n] for n in nums]
"""
#Leetcode Copied sultion 13900 kb
"""
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output_count = []
        count = 0
        for i in range(len(nums)) :
            for j in nums:
                if nums[i] > j :
                    count += 1
            output_count.append(count)
            count = 0
        return output_count    
"""
