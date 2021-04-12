"""
Runtime: 48 ms, faster than 32.40% of Python3 online submissions for Special Array With X Elements Greater Than or Equal X.
Memory Usage: 14.4 MB, less than 20.30% of Python3 online submissions for Special Array With X Elements Greater Than or Equal X.
"""
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        ans=-1
        for x in range(len(nums)+1):
            count=0
            for i in range(len(nums)):
                if x<=nums[i]:
                    count+=1
                    if x <= count:
                        ans=x
                        if x<count:
                            ans=-1
                            break
        return ans
