class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        
        def backtrack(candidates,idx,l,remain):
            for i in range(idx,len(candidates)):
                if candidates[i]==remain:
                    ans=l+[candidates[i]]
                    if ans not in res:
                        res.append(ans)
                elif candidates[i]<remain:
                    backtrack(candidates,i,l+[candidates[i]],remain-candidates[i])
                    
        
        backtrack(candidates,0,[],target)
        return res
