# use primes to give a unique value to each letter.
# then the word becomes a multiplication of those primes, without chance of collisions.
# permutations have same multiplication of primes since they're made of the same prime numbers underneath.

# Technically n squared but way faster than any default sort algorithm.
# we're only doing multiplications and comparisons of numbers.

# and trust me, computers are good at multiplying and if-else statements!

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letterToPrime = {
            "a": 2,
            "b": 3,
            "c": 5,
            "d": 7,
            "e": 11,
            "f": 13,
            "g": 17,
            "h": 19,
            "i": 23,
            "j": 29,
            "k": 31,
            "l": 37,
            "m": 41,
            "n": 43,
            "o": 47,
            "p": 53,
            "q": 59,
            "r": 61,
            "s": 67,
            "t": 71,
            "u": 73,
            "v": 79,
            "w": 83,
            "x": 87,
            "y": 89,
            "z": 97
        }

        result = {}

        for word in strs:
            total = 1
            for letter in word:
                total *= letterToPrime[letter]
            if total not in result:
                result[total] = [word]
            else:
                result[total].append(word)
        
        return list(result.values())