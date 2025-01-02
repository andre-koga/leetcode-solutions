# just recycling from problem 46. very slow obviously, being
# better than 22% of solutions only

# didn't bother to find a better solution lol, but again
# the idea is to backtrack

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 1:
            return [nums]

        # copy from previous. i know i could optimize but whatever

        result = self.rPermuteUnique(nums)
        finalResult = []
        for r in result:
            finalResult.append(tuple(r))
        return set(finalResult)

    def rPermuteUnique(self, numsLeft: List[int]) -> List[List[int]]:
            m = len(numsLeft)
            if m == 2:
                return [numsLeft, numsLeft[::-1]]
            
            result = self.rPermuteUnique(numsLeft[1:])
            nextResult = []
            for perm in result:
                for j in range(m):
                    nextResult.append(perm[:j] + [numsLeft[0]] + perm[j:])
            
            return nextResult
