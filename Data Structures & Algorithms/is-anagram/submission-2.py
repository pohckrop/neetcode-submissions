class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1=sorted(list(s))
        l2=sorted(list(t))
        
        if l1 == l2:
            return True
        else:
            return False