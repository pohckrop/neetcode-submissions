class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        num = set()

        print(nums)
        if nums:
            count,maxcount = 1,1
        else:
            count, maxcount = 0,0



        for i in range(1,len(nums)):
            print("diff: ", nums[i]-nums[i-1])
            if nums[i]-nums[i-1] == 1:
                count+=1
                print("count", count)    

            elif nums[i]-nums[i-1] == 0:
                print("equal")

            if count > maxcount:
                maxcount = count

            if nums[i]-nums[i-1] != 0 and nums[i]-nums[i-1] != 1:
                count = 1
                print("reset")

            
            

            

        return maxcount

        