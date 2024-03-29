"""
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.

"""
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        lst=[]
        for i in range(0,len(nums),2):
            lst += [nums[i+1]]*nums[i]
        return lst
#After 11 months code
"""    
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompress=[]
        for i in range(0,len(nums),2) :
            decompress += nums[i]*[nums[i + 1]]
        return decompress
"""
