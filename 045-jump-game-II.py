# approx better than 65% of submissions in matter of speed.

# not the most efficient, but it works.

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        furthest = 0
        jumps = 0
        currents = {0}

        while True:
            newSet = set()
            jumps += 1
            for current in currents:
                newSet.update(range(furthest, current + nums[current] + 1))
                furthest = max(furthest, current + nums[current])
                if furthest >= n - 1:
                    return jumps
            currents = newSet