"""
1347. Minimum Number of Steps to Make Two Strings Anagram

Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
"""

from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hashtable_s=Counter(s)
        steps=0
        for key,value in hashtable_s.items():
            tmp=t.count(key)
            if hashtable_s[key]>tmp:
                steps+=hashtable_s[key]-tmp
        return steps
        
