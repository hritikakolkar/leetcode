class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n=len(arr)
        m=int(n//20)
        arr.sort()
        return sum(arr[m:-1*m])/(n-2*m)
      
   
