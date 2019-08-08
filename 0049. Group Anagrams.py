class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        for i in strs:
            if tuple(sorted(i)) in d:
                d[tuple(sorted(i))].append(i)
            else:
                d[tuple(sorted(i))]=[i]
                

        return d.values()
