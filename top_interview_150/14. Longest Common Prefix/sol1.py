class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        minLength = 201

        for i in range(0,len(strs)):
            if len(strs[i]) < minLength:
                minLength = len(strs[i])
        
        resultingStringAr = ""
        
        i = 0
        
        while i < minLength:
            compareChar = strs[0][i]
            for word in strs:
                if word[i] == compareChar:
                    continue
                else:
                    return resultingStringAr
            resultingStringAr+=compareChar
            i+=1

        return resultingStringAr