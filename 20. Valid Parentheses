class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d={")":"(","]":"[","}":"{"}
        l=[]
        for i in s:
            if i in d:
                if len(l)<1:
                    return False
                if l[-1]==d[i]:
                    l.pop()
                else:
                    return False
            else:
                l.append(i)
                
        return True if l==[] else False 
