class Solution:
    def romanToInt(self, s: str) -> int:
        pairs = {
            "CM": 900,
            "CD": 400,
            "XC": 90,
            "XL": 40,
            "IX": 9,
            "IV": 4,
        }
        singles = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }
    
        result = 0
        while s != "":
            if len(s) >= 2 and s[-2:] in pairs.keys():
                result += pairs[s[-2:]]
                s = s[0: -2]
            else:
                result += singles[s[-1:]]
                s = s[0: -1]
            
            if len(s) == 0:
                return result
        