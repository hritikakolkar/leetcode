"""
Runtime: 76 ms, faster than 40.29% of Python3 online submissions for Duplicate Zeros.
Memory Usage: 15 MB, less than 34.56% of Python3 online submissions for Duplicate Zeros.
"""
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 1
        n = len(arr)
        while i < n :
            if arr[i-1] == 0 :
                arr.insert(i, 0)
                arr.pop()
                i+=2
            else:
                i+=1
                
"""
Runtime: 72 ms, faster than 58.43% of Python3 online submissions for Duplicate Zeros.
Memory Usage: 15 MB, less than 34.56% of Python3 online submissions for Duplicate Zeros.
"""
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        N = len(arr)
        
        for i in range(N-1, -1, -1):
            if i + zeros < N:
                arr[i+zeros] = arr[i]  
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < N:
                    arr[i+zeros] = 0
