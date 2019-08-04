class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        lookup={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno",
                "7":"pqrs","8":"tuv","9":"wxyz"}
        if digits=="":
            return []
        ans=[""]
        for i in digits:
            temp=[]
            for j in ans:
                temp+=[j+x for x in lookup[i]]
            ans=temp
            
        return ans
