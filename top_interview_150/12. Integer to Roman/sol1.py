class Solution:
    def intToRoman(self, num: int) -> str:
        mapper = {
            0: {
                1: "I",
                5: "V",
                4: "IV",
                9: "IX"
            },
            1: {
                1: "X",
                5: "L",
                4: "XL",
                9: "XC"
            },
            2: {
                1: "C",
                5: "D",
                4: "CD",
                9: "CM"
            },
            3: {
                1: "M"
            }

        }

        numStr = str(num)
        solAr = []

        counter = 0
        for i in range(len(numStr)-1,-1,-1):
            modded= int(numStr[i]) % 5
            if int(numStr[i]) < 4:
                solAr+=mapper[counter][1]*modded
            elif int(numStr[i]) == 4:
                solAr.append(mapper[counter][4])
            elif int(numStr[i]) < 9:
                solAr+=mapper[counter][1]*modded
                solAr.append(mapper[counter][5])
            else:
                solAr.append(mapper[counter][9])
            counter+=1
        solAr.reverse()
        finalSol=''.join(solAr)
        return finalSol