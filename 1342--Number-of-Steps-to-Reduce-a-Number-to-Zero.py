"""
1342. Number of Steps to Reduce a Number to Zero
Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it. 
"""
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        if int(num)==0:
            return count
        if num%2==0:
            count+=1
            return count + self.numberOfSteps(num/2)
        else:
            count+=1
            return count + self.numberOfSteps(num-1)
