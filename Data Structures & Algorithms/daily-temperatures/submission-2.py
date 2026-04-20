class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)

        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stemp, sindex = stack.pop()
                output[sindex] = i-sindex
            stack.append([t,i])
        return output



            
            

            
        