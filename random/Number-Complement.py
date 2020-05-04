"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
"""

class Solution:
    def findComplement(self, num: int) -> int:
        binary_rep_num=[]
        while num>=1:
            binary_rep_num.append(str(num%2))
            num=num//2
        def complement(string):
            ans=""
            for i in string:
                if i=="0":
                    ans+="1"
                else :
                    ans+="0"
            return ans
        list(reversed(binary_rep_num))
        return int(complement("".join(list(reversed(binary_rep_num)))),2)
