# very simple solution (i think 26 could've followed a similar and cleaner approach? or maybe not)
# two pointers, one looks for valid numbers, the other just stays in the index to be used

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left, right = 0, 0
        while right < n:
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            right += 1

        return left