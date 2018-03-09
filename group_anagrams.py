""" Given an array of strings, group anagrams together."""

from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grouped_words = defaultdict(list)
        for word in strs:
            grouped_words["".join(sorted(word))].append(word)
    
        return grouped_words.values()
        
""" Comment:
The cleanest way is to build a defaultdict with default factory as a list.
Use sorted values of the strings as keys. This way all anagrams are grouped together. """
