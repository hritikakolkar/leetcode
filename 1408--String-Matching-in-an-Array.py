"""
1408. String Matching in an Array

Given an array of string words. Return all strings in words which is substring of another word in any order. 

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].
"""


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans_lst=[]
        for word in words:
            for word2 in words:
                if not word==word2:
                    if word in word2 :
                        ans_lst.append(word)
        return list(set(ans_lst))
