class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        
        def backtrack(combination,n_left,n_right):
            if n_left==n and n_right==n:
                output.append(combination)
            elif n_left==n:
                backtrack(combination+')',n_left,n_right+1)
            elif n_right==n_left:
                backtrack(combination+'(',n_left+1,n_right)
            
            else:
                backtrack(combination+'(',n_left+1,n_right)
                backtrack(combination+')',n_left,n_right+1)
                    
        
        output=[]
        backtrack("",0,0)
                
        return output
