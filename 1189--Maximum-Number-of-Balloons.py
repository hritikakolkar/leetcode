"""
1189. Maximum Number of Balloons

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_count={
             "b":0,
             "a":0,
             "l":0,
             "o":0,
             "n":0
                   }
        for i in text:
            if i in "balon":
                char_count[i]+=1
        char_count["l"]=char_count["l"]//2
        char_count["o"]=char_count["o"]//2    
        return min(char_count.values())
