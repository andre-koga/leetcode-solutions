# easy problem, just do binary search with some extra if cases so we never return -1
# better than 85% in memory!
# (my own, original solution)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return n

        l, r = 0, n - 1
        
        while l <= r:
            m = (l + r) >> 1
            if nums[m] == target:
                return m
            elif nums[m] > target:
                if nums[m - 1] < target:
                    return m
                r = m - 1
            else:
                if nums[m + 1] > target:
                    return m + 1
                l = m + 1