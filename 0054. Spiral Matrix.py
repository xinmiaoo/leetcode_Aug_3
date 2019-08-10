class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix==[]:
            return []
        res=[]
        row,col=len(matrix),len(matrix[0])
        i,j,m,n=0,row-1,0,col-1
        
        while(1):
            for k in range(m,n+1):
                res.append(matrix[i][k])
            i+=1
            
            if i>=j+1 or m>=n+1:
                break
            for k in range(i,j+1):
                res.append(matrix[k][n])
            n-=1
            if i>=j+1 or m>=n+1:
                break
                
            for k in range(n,m-1,-1):
                res.append(matrix[j][k])
            j-=1
            if i>=j+1 or m>=n+1:
                break
                
            for k in range(j,i-1,-1):
                res.append(matrix[k][m])
            m+=1
            if i>=j+1 or m>=n+1:
                break

            
        return res
