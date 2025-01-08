# This solution involves three pointers.
# The first pointer shows where we're putting the final elements at
# the left pointer shows the number we just put
# the right pointer looks for different numbers, and it keeps growing until it finds
# a different number.
# the left pointer is necessary bc while nums[pointer] == nums[left], not necessarily
# nums[pointer + 1] == nums[left + 1]

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1

        pointer = 0
        left = 0
        right = 1

        while right < n:
            pointer += 1
            while nums[left] == nums[right]:
                right += 1
                if right == n:
                    return pointer
            # nums[left] != nums[right]
            nums[pointer] = nums[right]
            left = right
            right += 1
        
        return pointer + 1