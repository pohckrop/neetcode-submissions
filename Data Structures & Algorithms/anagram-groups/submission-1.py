class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = defaultdict(list)
        
        for s in strs:

            counter = [0] * 26

            for letter in s:
                counter[ord(letter)-ord('a')]+=1
            
            memo[tuple(counter)].append(s)
        
        return memo.values()

            

            


        
        

       
           



        
        