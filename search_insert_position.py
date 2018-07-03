# Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0 
        right = len(nums) - 1
        while left <= right: # usual condition for binary search
            mid = (left + right)//2
            if nums[mid] < target: # Look in the right half. Position will be in the beginning of the array
                left = mid + 1
                pos = mid + 1
            elif nums[mid] > target: # Look in the left half. Position will be at the end of the array
                right = mid - 1
                pos = mid
            else:
                return mid
        return pos
