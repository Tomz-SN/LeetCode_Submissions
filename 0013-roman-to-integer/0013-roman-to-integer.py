class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        i = -1
        while i < len(s) - 1:
            i += 1
            if i !=len(s)-1:
                if s[i] == "I":
                    if s[i+1] == "V":
                        value += 4
                        i += 1
                        continue
                    elif s[i+1] == "X":
                        value += 9
                        i +=1
                        continue
                    else:
                        value += 1
                        continue
                elif s[i] == "X":
                    if s[i+1] == "L":
                        value += 40
                        i += 1
                        continue
                    elif s[i+1] == "C":
                        value += 90
                        i +=1
                        continue
                    else:
                        value += 10
                        continue
                elif s[i] == "C":
                    if s[i+1] == "D":
                        value += 400
                        i += 1
                        continue
                    elif s[i+1] == "M":
                        value += 900
                        i +=1
                        continue
                    else:
                        value += 100
                        continue
            if s[i] == "I":
                value += 1
            elif s[i] == "V":
                value += 5
            elif s[i] == "X":
                value += 10
            elif s[i] == "L":
                value += 50
            elif s[i] == "C":
                value += 100
            elif s[i] == "D":
                value += 500
            elif s[i] == "M":
                value += 1000 
        return value


        