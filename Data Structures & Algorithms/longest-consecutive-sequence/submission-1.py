class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset=set(nums)
        longest=0

        for n in nset:
            if n-1 not in nset:
                length=1
                while n+1 in nset:
                    length+=1
                    n+=1
                longest=max(length, longest)
        return longest
        