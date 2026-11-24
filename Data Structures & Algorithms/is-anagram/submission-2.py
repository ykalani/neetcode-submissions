class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = []
        count = 0 
        s = sorted(s)
        t = sorted(t)
        if s == t: 
            return True 
        else: 
            return False
                    
                
        