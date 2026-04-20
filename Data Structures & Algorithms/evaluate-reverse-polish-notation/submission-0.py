class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i in ("+","-","*","/"):
                a=int(stack.pop())
                b=int(stack.pop())
                if i == "+":
                    stack.append(a+b)
                if i == "-":
                    stack.append(b-a)
                if i == "*":
                    stack.append(a*b)
                if i == "/":
                    stack.append(b/a)

            if i not in ("+","-","*","/"):
                stack.append(i)
        return int(stack[0])