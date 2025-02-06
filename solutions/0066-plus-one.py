# simple solution, 0ms, beats all other solutions (100%)
# we just need to add 1 to the last digit, and then iterate through the digits, adding 1 to the next digit if the current digit is 10
# if we reach the end of the list, we add a 1 to the beginning of the list
# we can do this in O(n) time
# we can also do this in O(1) space, since we're modifying the input list in place

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        
        n = len(digits)
        d = 1

        while digits[-d] == 10:
            digits[-d] = 0
            d += 1
            if d > n:
                digits.insert(0, 1)
                break
            digits[-d] += 1

        return digits