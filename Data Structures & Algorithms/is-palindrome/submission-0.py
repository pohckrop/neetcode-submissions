class Solution:
    def isPalindrome(self, s: str) -> bool:
        counter = 0
        s=s.lower()
        ar=[]
        for i in s:
            if i.isalnum()==True:
                ar+=i
        
        for i in range(len(ar)):
            if ar[i] == ar[-i-1]:
                continue
            else:
                return False

        return True
            
        