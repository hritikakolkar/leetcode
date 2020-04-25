"""
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.
"""

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        def right1(stri,mov):
            return stri[-1*mov:] + stri[:-1*mov]
        def left0(stri,mov):
            return stri[mov:] + stri[:mov]
        for i in shift:
            if i[0]==1:
                s=right1(s,i[1])
            elif i[0]==0:
                s=left0(s,i[1])
        return s
