class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        n = len(nums)
        result = set()
        nums.sort()

        for i in range(n):
            for j in range(i + 1, n):
                k = j + 1
                l = n - 1
                while k < l:
                    comp = nums[i] + nums[j] + nums[k] + nums[l]
                    if comp == target:
                        result.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
                    elif comp > target:
                        l -= 1
                    else:
                        k += 1
        return result