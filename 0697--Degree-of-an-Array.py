"""
Runtime: 220 ms, faster than 88.84% of Python3 online submissions for Degree of an Array.
Memory Usage: 15.4 MB, less than 73.28% of Python3 online submissions for Degree of an Array.
"""
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        start, end, freq, ans = {}, {}, {}, len(nums)
        for idx, num in enumerate(nums) :
            freq[num] = freq.get(num,0) + 1
            if num not in start :
                start[num] = idx
            end[num] = idx
        maxFreq = max(freq.values())
        maxFreqList = []
        for key, value in freq.items() :
            if value == maxFreq :
                maxFreqList.append(key)
        for key in maxFreqList :
            ans = min(ans, end[key] - start[key])
        return ans + 1

"""
Runtime: 232 ms, faster than 67.01% of Python3 online submissions for Degree of an Array.
Memory Usage: 15.2 MB, less than 98.07% of Python3 online submissions for Degree of an Array.
"""
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        start, end, freq, ans = {}, {}, {}, len(nums)
        for idx, num in enumerate(nums) :
            freq[num] = freq.get(num,0) + 1
            if num not in start :
                start[num] = idx
            end[num] = idx
        degree = max(freq.values())
        for key, value in freq.items() :
            if value == degree :
                ans = min(ans, end[key] - start[key])
        return ans + 1
