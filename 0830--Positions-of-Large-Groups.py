"""
Runtime: 36 ms, faster than 80.79% of Python3 online submissions for Positions of Large Groups.
Memory Usage: 14.1 MB, less than 95.44% of Python3 online submissions for Positions of Large Groups.
"""
class Solution(object):
    def largeGroupPositions(self, S):
        ans = []
        i = 0 # The start of each group
        for j in range(len(S)):
            if j == len(S) - 1 or S[j] != S[j+1]:
                # Here, [i, j] represents a group.
                if j-i+1 >= 3:
                    ans.append([i, j])
                i = j+1
        return ans
    
"""
Runtime: 32 ms, faster than 93.07% of Python3 online submissions for Positions of Large Groups.
Memory Usage: 14.3 MB, less than 63.43% of Python3 online submissions for Positions of Large Groups.
"""
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        if len(s)<3:
            return []
        ans = list()
        start = 0
        count = 1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
                if count>=3:
                    if i != len(s)-1 :
                        if s[i] != s[i+1]:
                            ans.append([start,i])
                    else:
                        ans.append([start,i])
            else:
                start = i
                count = 1
        return ans
