class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        conversion = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        output = [""]
        for digit in digits:
            letters = conversion[digit]
            newOutput = []
            for sequence in output:
                for letter in letters:
                    newOutput.append(sequence + letter)
            output = newOutput

        return output