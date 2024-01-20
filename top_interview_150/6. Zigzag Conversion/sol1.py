class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lenStr = len(s)
        rotation = numRows + (numRows - 2)
        solStrings = [[]]
        
        if numRows == 1:
            return s

        
        middlePoint = math.ceil(rotation/2)
        for i in range(lenStr):
            
            if i % rotation <= middlePoint: 
                netI = i % rotation
                if len(solStrings) <= i % rotation:
                    solStrings.append([])
                solStrings[netI].append(s[i])

            elif  i % rotation > middlePoint:
                netI = middlePoint - (i % middlePoint )
                solStrings[netI].append(s[i])



        solString = ""

        for subAr in solStrings:
            solString += "".join(subAr)

        return solString