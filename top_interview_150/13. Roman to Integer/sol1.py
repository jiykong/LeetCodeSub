class Solution:
    def romanToInt(self, s: str) -> int:
        mapper = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        i = 0 
        totalSum = 0
        while i < len(s):
            if s[i] == "I" and i!= len(s) - 1 and (s[i+1] =="V" or s[i+1] =="X"):
                totalSum+= mapper[s[i+1]] - 1
                i+=2;
            elif s[i] == "X" and i!= len(s) - 1 and (s[i+1] =="L" or s[i+1] =="C"):
                totalSum+= mapper[s[i+1]] - 10
                i+=2;
            elif s[i] == "C" and i!= len(s) - 1 and (s[i+1] =="D" or s[i+1] =="M"):
                totalSum+= mapper[s[i+1]] - 100
                i+=2;
            else:
                totalSum+= mapper[s[i]]
                i+=1
            

        return totalSum

