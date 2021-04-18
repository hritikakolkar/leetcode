"""
Runtime: 384 ms, faster than 25.38% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 21.9 MB, less than 72.80% of Python3 online submissions for Find All Numbers Disappeared in an Array.
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            idx = abs(nums[i])-1
            nums[idx] = -abs(nums[idx])
        return [i+1 for i in range(len(nums)) if nums[i]>0]
        """
        length = len(nums)
        n = 0
        check = 1
        ans=[]
        while n<length and check<=length:
            if nums[n] == check:
                n+=1
                check+=1
            elif nums[n] < check :
                if n==length-1:
                    ans.append(check)
                n+=1
            else:
                ans.append(check)
                check+=1
        return ans
        """

"""
Runtime: 312 ms, faster than 99.16% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 26.3 MB, less than 5.29% of Python3 online submissions for Find All Numbers Disappeared in an Array.
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return set(range(1,len(nums)+1))-set(nums)
