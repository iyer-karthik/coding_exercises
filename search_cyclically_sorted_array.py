""" 
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
"""

class Solution(object):
    
    def search_smallest_element_index(self, nums):
        left = 0
        right = len(nums) - 1 
        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return left
    
    def bin_search(self, modified_nums, target):
        left = 0 
        right = len(modified_nums) - 1
        while left <= right:
            mid = (left + right)//2
            if modified_nums[mid] == target:
                return mid
            elif modified_nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
                    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        smallest_element_index = self.search_smallest_element_index(nums)
        
        if nums == []:
            return -1
        elif nums[smallest_element_index] == target:
            return smallest_element_index
        elif nums[smallest_element_index] < target <= nums[-1]:
            shifted_index = self.bin_search(nums[smallest_element_index:], target)
            if shifted_index == -1:
                return -1
            else:
                return  smallest_element_index + shifted_index
        else:
            return self.bin_search(nums[:smallest_element_index], target)
            
"""
Comment:
-------
We use the cyclical sorted structure to first find the index of the smallest element. This 
can be done in O(log n) time. Once this is done, we know that the subarray to the right and 
to the to the left are both sorted. We can then do a binary search again in O(log n) time.
"""
