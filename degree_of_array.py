""" Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of 
its elements. Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums."""

from collections import Counter
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not(nums):
            return 0
        counter_dict = Counter(nums)
        max_frequency = max(counter_dict.values())
        result = float('inf')
        for key, value in counter_dict.items():
            if value == max_frequency:
                result = min(result, len(nums) - nums[::-1].index(key) - nums.index(key)) 
        return result
        
 """Comment: We interate through the loop and create a hash table containing the count of each element. 
 For elements with maximum count, we compute the length of the contiguous subarray starting and ending
 at those elements. We then take the minimum of all such lengths."""
