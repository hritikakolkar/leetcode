"""
1309. Decrypt String from Alphabet to Integer Mapping

Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.
"""
class Solution:
    def freqAlphabets(self, s: str) -> str:
        lst_num=[]
        n=len(s)
        i=n-1
        while i>=0:
            if s[i]=="#":
                lst_num.append(s[i-2:i])
                i-=3
            else:
                lst_num.append(s[i])
                i-=1
        print(lst_num)
        return  "".join(map(lambda x:str(chr(96+int(x))),lst_num))[::-1]
