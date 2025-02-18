class Solution(object):
    def romanToInt(self, s):
        numeros= {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }

        array= []
        o=0

        ##XXXVIII

        for s in s:
            array.append(s)


        for x in range(0,len(array)):
            try:
                if numeros[array[x]]<numeros[array[x+1]]:
                    o-=numeros[array[x]]
                else:
                    o+=numeros[array[x]]


            except:
                o+=numeros[array[x]]
        return o
        