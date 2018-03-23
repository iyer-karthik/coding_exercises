"""Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1]."""

class Solution(object):
    
    def search_range_left(self, nums, target):
        left = 0
        right = len(nums) - 1
        result = -1
        while left <=  right:
            mid  = left + (right - left)/2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                result = mid
                right = mid -1
            else:
                left = mid + 1
  
        return result
  
    def search_range_right(self, nums, target):
        left_index =  self.searchRangeleft(nums, target)
        #print left_index
        left = left_index 
        right = len(nums) - 1
        result = -1
        while left <=  right:
            mid  = left + (right - left)/2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                result = mid
                left = mid + 1 
            else:
                right = mid - 1
        return [left_index, result]
    
    def searchRange(self, nums, target):

        if self.searchRangeleft(nums, target) == -1:
            return [-1,-1]
        return self.searchRangeright(nums, target)
        
 """ Comment:
 We do a binary search twice. First to find the leftmost index and then to find the rightmost index. 
 For finding the leftmost index, proceed as in binary search but once you encounter the target, shift left.
 (This gives you the first index.) Finding out the rightmost index follows a similar logic. 
 """
