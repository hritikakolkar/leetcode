"""
1170. Compare Strings by Frequency of the Smallest Character

Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words
"""
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            return s.count(min(s))
        answer=[]
        for querie in queries:
            count=0
            for word in words:
                if f(querie)<f(word):
                    count+=1
            answer.append(count)
        return answer
