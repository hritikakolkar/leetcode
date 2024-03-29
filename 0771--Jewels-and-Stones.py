"""
Runtime: 32 ms, faster than 54.19% of Python3 online submissions for Jewels and Stones.
Memory Usage: 14.2 MB, less than 45.79% of Python3 online submissions for Jewels and Stones.
"""
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = {}
        for jewel in jewels:
            freq[jewel]=0
        for stone in stones:
            if stone in freq:
                freq[stone]+=1
        return sum(freq.values())
    
"""
Runtime: 16 ms, faster than 99.87% of Python3 online submissions for Jewels and Stones.
Memory Usage: 14.3 MB, less than 12.57% of Python3 online submissions for Jewels and Stones.
"""
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> list :
        return sum(s in jewels for s in stones)







