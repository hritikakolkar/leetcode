"""
728. Self Dividing Numbers

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
"""

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        def self_dividing(num):
            s_num=str(num)
            x=True
            if "0"in s_num:
                return False
            for i in s_num:
                if int(s_num)%int(i)==0:
                    x= True and x
                else:
                    x= False and x
            return x
        for i in range(left,right+1):
            if self_dividing(i):
                ans.append(i)
        return ans
