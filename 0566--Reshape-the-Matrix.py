"""
Runtime: 104 ms, faster than 29.32% of Python3 online submissions for Reshape the Matrix.
Memory Usage: 15.4 MB, less than 17.88% of Python3 online submissions for Reshape the Matrix.
"""
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums)*len(nums[0]) != r*c: return nums
        m, n = len(nums), len(nums[0])
        one_d=[]
        ans=[]
        for row in nums:
            one_d+=row
        temp=0
        for row in range(r):
            temp=[]
            for col in range(c):
                temp.append(one_d.pop(0))
            ans.append(temp)
        return ans
                
"""
Runtime: 84 ms, faster than 99.39% of Python3 online submissions for Reshape the Matrix.
Memory Usage: 15.1 MB, less than 92.58% of Python3 online submissions for Reshape the Matrix.
"""
class Solution(object):
    def matrixReshape(self, nums, r, c):
        if r * c != len(nums) * len(nums[0]):
            return nums
        result = []
        row = []
        for num in nums:
            for n in num:
                row.append(n)
                if len(row) == c:
                    result.append(row)
                    row = []
        return result
