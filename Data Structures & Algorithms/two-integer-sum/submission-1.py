class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum=0
        for n1 in range(len(nums)):

            for n2 in range(len(nums)):

                if nums[n1]+nums[n2] == target and n1 != n2:
                    return [n1,n2]
        