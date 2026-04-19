class Solution:

    def encode(self, strs: List[str]) -> str:
        string=""
        for i in strs:
            string+=(i+"314159")
        print(string)
        return string    

    def decode(self, s: str) -> List[str]:
        output = s.split("314159")
        output.pop()
        return output

        