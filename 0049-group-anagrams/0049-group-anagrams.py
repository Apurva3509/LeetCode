from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram = defaultdict(list)
        result =[]

        for s in strs:
              sorted_s = tuple(sorted(s)) # gives a list object back so we use tuple to make it immutable
              anagram[sorted_s].append(s)
        
        for value in anagram.values():
            result.append(value)

        return result
