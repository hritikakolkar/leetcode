class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest=0
        summation=0
        for altitude in gain:
            summation+=altitude
            if summation > highest:
                highest = summation
        return highest
        
