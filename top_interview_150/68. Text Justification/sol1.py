class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        lineLength = 0
        wordLengths = 0
        wordCount = 0

        lineArr = []
        solArr = []
        for text in words:
            if wordCount != 0:
                lineLength+=1
            lineLength += len(text)
            if maxWidth < lineLength:
                spaceCount = (maxWidth - wordLengths)
                if wordCount > 2:

                    if spaceCount%(wordCount-1) != 0:
                        tmpStr = ""

                        tmpStr += (" " * math.ceil(spaceCount/(wordCount-1))).join(lineArr[0:(spaceCount%(wordCount-1))+1])
                        if len(lineArr[spaceCount%(wordCount-1)+1:]) == 1:
                            tmpStr += " " * (spaceCount//(wordCount-1)) + lineArr[-1]
                        else:    
                            tmpStr += (" " * (spaceCount//(wordCount-1))) + (" " * (spaceCount//(wordCount-1))).join(lineArr[spaceCount%(wordCount-1)+1:])
                        solArr.append(tmpStr)

                    else:
                        solArr.append((" " * (spaceCount//(wordCount-1))).join(lineArr))

                elif wordCount == 2:
                    solArr.append(lineArr[0] + " " * spaceCount + lineArr[1])
                elif wordCount == 1:
                    solArr.append(lineArr[0] + " " * spaceCount)

                wordCount = 0
                wordLengths = 0
                lineLength = len(text)
                lineArr = []
                
            wordCount +=1
            wordLengths += len(text)
            lineArr.append(text)
        solArr.append((" ".join(lineArr) + " " * (maxWidth - lineLength) ))
        return solArr