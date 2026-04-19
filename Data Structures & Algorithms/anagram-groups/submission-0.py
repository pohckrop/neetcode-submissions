class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo=defaultdict(list)
        for s in strs:
            count = [0] * 26

            for c in s:
                print(c)
                count[ord(c)-ord("a")]+=1

            memo[tuple(count)].append(s)
            
        return memo.values()


        
        

       
           



        
        