class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        splitStack = haystack.split(needle)
        if len(splitStack) == 1:
            return -1

        else:
            return len(splitStack[0])