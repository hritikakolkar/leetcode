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
            
