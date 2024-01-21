class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        hashMap = {}
        i = 0
        for i in range(len(t)):
            if t[i] not in hashMap:
                hashMap[t[i]] = []
            hashMap[t[i]].append(i)

        latestMax = -1
        for i in range(len(s)):
            if s[i] in hashMap:
                locFound = False
                for loc in hashMap[s[i]]:
                    if loc > latestMax:
                        locFound = True
                        latestMax = loc
                        break
                    else:
                        locFound = False

                if locFound == False:
                    return False
            else:
                return False

        return True