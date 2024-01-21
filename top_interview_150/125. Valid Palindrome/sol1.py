class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s) - 1
        s = s.lower()
        while i < j:
            if s[i].isalpha() == False and s[i].isnumeric() == False:
                i+=1
                continue
            if s[j].isalpha() == False and s[j].isnumeric() == False: 
                j-=1
                continue
            
            if s[i] == s[j]:
                i+=1
                j-=1
                continue
            else:
                return False

        return True


