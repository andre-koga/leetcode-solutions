# pretty clever intuition:
# the idea is that once you are right in the middle of the numbers
# so that half is above, half is below, it doesn't matter anymore
# whether you move up or down; each step decreased in a number is countered
# by another number's step increasing. so this is the global minima, which suffices

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)

        target = nums[n // 2]
        answer = 0
        for num in nums:
            answer += abs(num - target)

        return answer
