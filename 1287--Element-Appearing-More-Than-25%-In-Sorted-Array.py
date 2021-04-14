"""
1287. Element Appearing More Than 25% In Sorted Array

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.
"""
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter_dictionary={}
        for element in arr:
            if element in counter_dictionary.keys():
                counter_dictionary[element]+=1
            else:
                counter_dictionary[element]=1
        for key,value in counter_dictionary.items():
            if value/len(arr)>0.25:
                return key
"""
Runtime: 80 ms, faster than 96.11% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
Memory Usage: 15.4 MB, less than 76.95% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
"""
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr)==1:return arr[0]
        temp=arr[0]
        count=1
        length = len(arr)
        for num in arr[1:]:
            if num == temp:
                count+=1
            else: 
                count=1
            if count/length > 0.25: return num
            temp=num
            
            
