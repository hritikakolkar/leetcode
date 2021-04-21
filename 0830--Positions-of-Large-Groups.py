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
