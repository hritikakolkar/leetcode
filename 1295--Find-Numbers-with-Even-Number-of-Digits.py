"""
Given an array nums of integers, return how many of them contain an even number of digits.
"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if len(str(i))%2==0:
                count+=1
        return count

#Solved after 11 months    
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        """
        ans=0
        for num in nums:
            if len(str(num))%2==0:
                ans+=1
        return ans
        """
        ans=0
        for num in nums:
            length=0
            temp=1
            while temp <=num:
                length+=1
                temp*=10
            if length%2==0:
                ans+=1
        return ans
