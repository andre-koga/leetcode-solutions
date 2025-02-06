class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while (left < right):
                temp = nums[i] + nums[left] + nums[right]
                if temp == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif (temp > 0):
                    right -= 1
                else:
                    left += 1
        return result