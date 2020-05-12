"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        lst_s=list(s)
        start=0
        end=len(lst_s)-1
        while start<end:
            start__=lst_s[start] in "aeiouAEIOU"
            end__=lst_s[end] in "aeiouAEIOU"
            if start__ and end__ :
                lst_s[start],lst_s[end]=lst_s[end],lst_s[start]
                start+=1
                end-=1
            elif (not start__) and end__:
                start+=1
            elif start__ and (not end__):
                end-=1
            else:
                start+=1
                end-=1
        return "".join(lst_s)
                
                
