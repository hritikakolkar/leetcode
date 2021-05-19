"""
Runtime: 68 ms, faster than 24.22% of Python3 online submissions for Check If N and Its Double Exist.
Memory Usage: 14.4 MB, less than 16.54% of Python3 online submissions for Check If N and Its Double Exist.
"""
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for idx in range(len(arr)) :
            for jdx in range(idx+1,(len(arr))) :
                if arr[idx] == arr[jdx]*2 or arr[idx]== arr[jdx]/2 :
                    return True
        return False
