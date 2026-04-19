class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        num = set()

        print(nums)
        if not nums:
            return 0
        count = 1
        maxcount = 1

        for i in range(1,len(nums)):
            if nums[i]-nums[i-1] == 1:
                count+=1

            if count > maxcount:
                maxcount = count

            if nums[i]-nums[i-1] != 0 and nums[i]-nums[i-1] != 1:
                count = 1

        return maxcount

        