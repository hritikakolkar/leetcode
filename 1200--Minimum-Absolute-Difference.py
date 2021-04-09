#Time Limit Exceeded
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mad=10000000
        for i in range(1,len(arr)):
            mad=min(mad,arr[i]-arr[i-1])
        ans=list()
        for idx in range(len(arr)):
            for jdx in range(idx+1,len(arr)):
                if arr[idx]<arr[jdx] and arr[jdx]-arr[idx]==mad:
                    ans.append([arr[idx],arr[jdx]])
        return ans
    
"""
Runtime: 380 ms, faster than 21.94% of Python3 online submissions for Minimum Absolute Difference.
Memory Usage: 28.1 MB, less than 62.25% of Python3 online submissions for Minimum Absolute Difference.
"""
class Solution1:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mad=10000000
        for i in range(1,len(arr)):
            mad=min(mad,arr[i]-arr[i-1])
        ans=list()
        for idx in range(1,len(arr)):
            if arr[idx]-arr[idx-1]==mad:
                    ans.append([arr[idx-1],arr[idx]])
        return ans
    
"""
Runtime: 312 ms, faster than 97.63% of Python3 online submissions for Minimum Absolute Difference.
Memory Usage: 28.2 MB, less than 62.25% of Python3 online submissions for Minimum Absolute Difference.
"""
class Solution2:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        temp = arr[0]
        mad = 2*(10**6)
        ans=list()
        for num in arr[1:]:
            diff =num -temp
            if mad == diff :
                ans.append([temp,num])
            if mad>diff:
                mad=diff
                ans=[[temp,num]]
            temp=num
        return ans
