class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best = 99999
        for i, num in enumerate(nums):
            left = 0
            right = len(nums) - 1
            while (left < right):

                if left == i:
                    left += 1
                    continue
                elif right == i:
                    right -= 1
                    continue

                comp = num + nums[left] + nums[right]
                if abs(comp - target) < abs(best - target):
                    best = comp
                    if best == target:
                        return best
                if comp < target:
                    left += 1
                else:
                    right -= 1
        return best
                