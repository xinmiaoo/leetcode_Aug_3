class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashTable={}
        start=0
        max_l=0
        for i in range(len(s)):
            if s[i] not in hashTable:
                hashTable[s[i]]=i
                max_l=max(i-start+1,max_l)
            else:
                if hashTable[s[i]]>=start:
                    start=hashTable[s[i]]+1
                hashTable[s[i]]=i
                max_l=max(i-start+1,max_l)
        return max_l
