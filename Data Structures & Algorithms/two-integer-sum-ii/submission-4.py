class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index = {}

        for i,n in enumerate(numbers):
            index[n] = i

        for i,n in enumerate(numbers):
            diff = target - n
            if diff in index and index[diff] != i:
                return [i+1, index[diff]+1]
        
