class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if intervals==[]:
            return []
        intervals.sort(key=lambda x: x[0])
        
        res=[intervals[0]]
        if len(intervals)==1:
            return res
        for i in range(1,len(intervals)):

            if intervals[i][0]<=res[-1][1]:
                if intervals[i][0]>=res[-1][0]:
                    temp=max(res[-1][1],intervals[i][1])
                    res[-1]=[res[-1][0],temp]
                else:
                    res[-1]=intervals[i]
                    
            else:
                res.append(intervals[i])
                
                
        return res
