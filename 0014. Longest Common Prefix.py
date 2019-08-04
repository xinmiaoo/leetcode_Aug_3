class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        common_pf=strs[0]
        
        for i in range(1,len(strs)):
            common_pf=self.cp(common_pf,strs[i])
            
        return common_pf
    
    
    def cp(self,s1,s2):
        i=0
        while(i<min(len(s1),len(s2))):
            if s1[i]==s2[i]:       
                i+=1
            else:
                break
              
        return s1[:i]
