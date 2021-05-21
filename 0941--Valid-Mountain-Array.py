"""
Runtime: 212 ms, faster than 23.39% of Python3 online submissions for Valid Mountain Array.
Memory Usage: 15.5 MB, less than 52.11% of Python3 online submissions for Valid Mountain Array.
"""
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        idx = 0
        n = len(arr)
        while idx<=n-2 and arr[idx] < arr[idx+1] :
            idx+=1
        if idx == 0 or idx == n-1 :
            return False
        while idx <= n-2  and arr[idx] > arr[idx+1] :
            idx+=1
        return idx == n-1
      
"""
Runtime: 244 ms, faster than 5.58% of Python3 online submissions for Valid Mountain Array.
Memory Usage: 15.3 MB, less than 95.88% of Python3 online submissions for Valid Mountain Array.
"""
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        peak, valley = 0, 0
        for i in range(1, len(A) - 1):
            if A[i - 1] < A[i] > A[i + 1]:
                peak += 1
            if A[i - 1] >= A[i] <= A[i + 1]:
                valley += 1
        return peak == 1 and valley == 0
