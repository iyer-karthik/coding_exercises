""" Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0."""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if s == "":
            return 0
            
        count = 0 
        right = len(s) - 1
        no_space = True
        
        # Ensure that the last character is not ' '
        while s[right] == ' ' and right >= 0:
            right = right - 1
        
        # Run a backward loop
        while right >=0 and no_space:
            if s[right] != ' ':
                count += 1
                right -= 1
            else:
                no_space = False
        return count
