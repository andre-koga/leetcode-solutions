# not my solution. i attempted to first find the pivot and "unrotate" the array, then perform
# the search. but it was too much of a hassle, with a lot of extra steps.
# this is the cleanest solution i found in the forum:

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # not my solution. learned from khadinhussaindev
        n = len(nums)

        l = 0
        r = n - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:
                # is the left half sorted?
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1