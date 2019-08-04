def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,
           "L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1, }
        
        ans=0
        while len(s)>1:
            if s[:2] in d:
                ans+=d[s[:2]]
                s=s[2:]
                continue
            if s[0] in d:
                ans+=d[s[0]]
                s=s[1:]
        
        if s:
            ans+=d[s]
            
        return ans
