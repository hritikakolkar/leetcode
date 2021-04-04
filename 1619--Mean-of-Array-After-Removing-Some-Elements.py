class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n=len(arr)
        m=int(n//20)
        arr.sort()
        return sum(arr[m:-1*m])/(n-2*m)
      
   
#From leet code copied for space complexity 97% using heapq
import heapq

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        
        hq_lo = []
        hq_up = []
        total = 0
        
        l = int(len(arr) * 0.05)
        r = len(arr) - 2 * l
        
        for n in arr:
            total += n
            heapq.heappush(hq_lo, -n)
            heapq.heappush(hq_up, n)
            if len(hq_lo) > l:
                heapq.heappop(hq_lo)
                heapq.heappop(hq_up)
                
        # print(total, hq_lo, hq_up, r)
                
        return (total + sum(hq_lo) - sum(hq_up)) / r
