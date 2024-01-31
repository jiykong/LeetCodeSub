class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        finalSol=0
        tmpSol = 0
        mapper = {}
        start = 0
        for i in range(len(s)):
            if ord(s[i]) not in mapper:
                mapper[ord(s[i])] = i
                tmpSol +=1

                
            elif start > mapper[ord(s[i])]:
                tmpSol +=1
                mapper[ord(s[i])] = i

            else:
                if tmpSol > finalSol:
                    finalSol = tmpSol
                start = mapper[ord(s[i])]
                tmpSol = i - mapper[ord(s[i])]
                mapper[ord(s[i])] = i

        
        if tmpSol > finalSol:
            finalSol = tmpSol

        return finalSol