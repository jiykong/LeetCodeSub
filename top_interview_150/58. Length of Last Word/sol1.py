class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s.rstrip()
        splitVal = s.split(" ")


        return (len(splitVal[-1]))
        