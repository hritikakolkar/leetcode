"""
1299. Replace Elements with Greatest Element on Right Side
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
 

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
"""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            arr[i]=max(arr[i+1:])
        arr[-1]=-1
        return arr

      
#Good Solution
"""
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return None
        
        max_val = arr[-1]
        
        for i in reversed(range(len(arr))):
            current = arr[i]
            arr[i] = max_val
            if max_val < current:
                max_val = current
                
        arr[-1] = -1 
        
        return arr
"""
