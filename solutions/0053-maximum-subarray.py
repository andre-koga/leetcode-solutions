# kadane's algorithm without using max - better than 98%!

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # lets do kadane's algorithm!

        # if we know the best subarray that ends in the index i,
        # then we can quickly calculate the best subarray that ends with i+1,
        # since:
        # - if the best subarray til i IS POSITIVE: best = best_til_i + nums[i+1]
        # - if the best subarray til i ISN'T POSITIVE: best = just nums[i+1]

        best_upto_i = -inf
        best_so_far = -inf

        for n in nums:
            best_upto_i = best_upto_i + n if best_upto_i + n > n else n
            if best_upto_i > best_so_far:
                best_so_far = best_upto_i

        return best_so_far

        # INTERESTINGLY, using max makes it way slower.