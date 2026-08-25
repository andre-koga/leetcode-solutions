class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # the contraints are pretty forgiving, i'll just do brute force
        num = k
        while num in nums:
            num += k

        return num
