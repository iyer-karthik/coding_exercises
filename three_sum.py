'''Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.'''


class Solution(object):
    
    def three_sum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if list(set(nums)) == [0] and len(nums) >= 3:
            return [[0,0,0]]
        else:
            result_arr = {}
            for i in range(0, len(nums) - 1):
                middle = i + 1
                right = len(nums) - 1
                while middle < right:
                    if nums[i] + nums[middle] + nums[right] == 0:
                        if (i, middle, right) not in result_arr:
                            result_arr[(i,middle,right)] = (nums[i], nums[middle], nums[right])
                        middle +=  1
                        right -= 1
                    elif nums[i] + nums[middle] + nums[right] > 0:
                        right -=  1
                    else:
                        middle +=  1
        
            return [list(x) for x in set(tuple(x) for x in result_arr.values())]
            # Convert to a tuple first as lists are not hashable. 
                

""" Comments: 
    The bruteforce solution is O(n^3) in complexity, which wasteful as it does a lot more comparisons than needed. One solution is to
    sort the given array (in place) and then advance from both ends of the array. This approach has time complexity O(n^2).
    """"
