"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        len_s=len(strs)
        if len_s==0: return ""
        if len_s==1: return strs[0]
        strs.sort()
        i=0
        len_o=len(strs[0])
        while i<len_o and strs[0][i]==strs[-1][i]:
            i+=1
        return strs[0][:i]
