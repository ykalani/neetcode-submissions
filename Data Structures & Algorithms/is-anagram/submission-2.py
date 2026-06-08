class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = 0 
        for i in s:  
            if s.count(i) == t.count(i): 
                count += 1 
            
        if count == len(s) and len(s) == len(t): 
            return True
        else: 
            return False        

