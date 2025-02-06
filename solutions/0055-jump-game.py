# better than 80%
# Time: O(n)
# Space: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # left pointer represents the index being currently checked
        # right pointer represents the furthest index we can go so far
        
        n = len(nums)
        if n <= 1:
            return True

        l, r = 0, 0

        while l <= r:
            if l + nums[l] > n - 2:
                return True
            elif l + nums[l] > r:
                r = l + nums[l]

            l += 1

        return False