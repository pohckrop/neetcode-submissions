class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            for n in numbers:
                if i != n:
                    if i+n==target:
                        return [(numbers.index(i)+1),(numbers.index(n)+1)]

        