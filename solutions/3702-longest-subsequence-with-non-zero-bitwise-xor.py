class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # the interesting observation to make here is that
        # if you have a sequence whose bitwise XOR is zero,
        # then you can just add another number to it that is non-zero
        # and that guarantees the XOR is non-zero; same happens with removing a number.
        # so we can be greedy and just try the whole sequence, if that doesn't work, we remove one number and that is it. of course, 0s change this situation

        if not any(nums):
            return 0

        result = 0
        n = len(nums)

        for num in nums:
            result ^= num

        if result != 0:
            return n
        else:
            return n - 1
