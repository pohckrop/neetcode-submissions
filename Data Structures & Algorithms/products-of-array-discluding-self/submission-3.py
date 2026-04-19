class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zerocount = 1,0
        output = [0] * len(nums)
        

        for n in nums:
            if n!=0:
                prod*=n
                continue
            zerocount+=1

        if zerocount > 1:
            return output
        
        for i,n in enumerate(nums):
            if zerocount > 0 and n!=0:
                output[i] = 0
            elif n == 0:
                output[i] = prod
            else:
                output[i] = int(prod/n)
        return output
