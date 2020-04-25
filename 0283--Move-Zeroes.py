  
"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        coun=nums.count(0)
        if coun!=0:
            for _ in range(coun):
                nums.remove(0)
            nums+=[0]*coun
            
