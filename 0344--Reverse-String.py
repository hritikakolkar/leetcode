"""
0344--Reverse-string.py

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        len_s=len(s)
        for i in range(len_s//2):
            temp=s[i]
            s[i]=s[len_s-i-1]
            s[len_s-i-1]=temp

#Write a function that reverses a string. The input string is given as an array of characters s.
#After 11 months soltuion
class Solution1:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        n=len(s)
        while i<=n//2-1:
            s[i],s[n-i-1]=s[n-i-1],s[i]
            i+=1
        
