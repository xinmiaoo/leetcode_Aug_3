class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res="1"
        if n==1:
            return res
        res="11"
        if n==2:
            return res
        for i in range(1,n-1): 
            temp=""
            accu=1
            curr=res[0]
            for j in range(1,len(res)):
                if res[j]!=curr:
                    temp+=str(accu)+curr
                    accu=1
                    curr=res[j]
                else:
                    accu+=1
            temp+=str(accu)+curr
            res=temp
            print res
        return res
