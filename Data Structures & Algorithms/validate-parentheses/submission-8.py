class Solution:
    def isValid(self, s: str) -> bool:
        lib = {")":"(",
                "]":"[",
                "}":"{"}

        stack=[]

        for c in s:
            if c in lib:
                if stack and stack[-1] == lib[c]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(c)    
        return stack == []



        
                

        




        