"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=int("".join(map(str,digits)))
        return list(str(num+1))\
        """
        if len(digits)==1:
            if digits[0]==9:
                return [1,0]
            else:
                digits[0]+=1
                return digits
        if digits[-1]!=9:
            digits[-1]+=1
        else:
            n=len(digits)-2
            digits[-1]=0
            while digits[n]==9 and n>=0:
                digits[n]=0
                n-=1
            if digits[n]==0:
                return [1]+digits
            else:
                digits[n]+=1
        return digits
        """
