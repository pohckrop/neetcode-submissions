class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        output = []
        for i in nums:
            count[i]+=1
        
        arr = []
        for i,n in count.items():
            arr.append([n,i])
        arr.sort()

        for i in range(k):
            print(arr[-1])
            output.append(arr.pop()[1])
        return output
            
            
