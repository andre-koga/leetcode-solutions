# im going to try recursion cus why not
# if we know how to find the permutation of n items
# then we can grab that list and add a new item in each index
# an n! amount of times. this generates all of the permutations
# of n + 1 items.
# keep that going and we will have the final requested set!

# this solution is O(n^2), not that good but whatevs

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 1:
            return [nums]

        return self.rPermute(nums)

    def rPermute(self, numsLeft: List[int]) -> List[List[int]]:
            m = len(numsLeft)
            if m == 2:
                return [numsLeft, numsLeft[::-1]]
            
            result = self.rPermute(numsLeft[1:])
            nextResult = []
            for perm in result:
                for j in range(m):
                    nextResult.append(perm[:j] + [numsLeft[0]] + perm[j:])
            
            return nextResult