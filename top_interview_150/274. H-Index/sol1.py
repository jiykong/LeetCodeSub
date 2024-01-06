class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort(reverse=True)
        print(citations)

        counter = 0
        for i in range(len(citations)):
            if (i+1) <= citations[i]:
                counter+=1
            else:
                break
                


        return counter 