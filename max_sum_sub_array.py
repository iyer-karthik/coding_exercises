"""Find the largest sum of a contiguous subarray within an array (containing at least one number)."""


class Solution(object):
    def max_sum_sub_array(self, nums):
        if len(nums) == 0:
            return 0
        current_sum = max_sum = nums[0]
        for j in range(1, len(nums)):
            # keep on adding till you add up to a negative number which is when you 'reset'
            current_sum = max(nums[j], current_sum + nums[j])  
            max_sum = max(max_sum, current_sum) # keeps track of the running maximum
        return max_sum

"""Comment:
This is a dynamic programming problem whose solution can be found in O(n) time. The key idea is to keep
track of the running sum and reset the running sum if it becomes less than 0. 
"""
