# better than ~90% of solutions regarding memory, better than ~50% regarding speed

# if a<b<c<... the next will be just flipping the last two digits
# if a>b>c>... we just mirror the number

# we look for the first occurrence from right to left of _,_,...,M,N,n,n,n,n...
# with M < N and n < N. Then we put the smallest digit found so far on M's position
# (bigger than M),
# then rearrange the remaining on the left side from smallest to biggest.

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        if n == 1:
            return
        
        i = n - 1
        while i > 0:
            if nums[i] <= nums[i - 1]:
                # nums still increasing from right to left
                i -= 1
            else:
                # found where to flip: M is idx - 1, N is idx
                j = n - 1
                while j >= i:
                    if nums[j] > nums[i - 1]:
                        nums[j], nums[i - 1] = nums[i - 1], nums[j]
                        # now we sort from smallest to biggest (rtl)
                        l, r = i, n - 1
                        while l < r:
                            nums[l], nums[r] = nums[r], nums[l]
                            l += 1
                            r -= 1
                        return
                    j -= 1
                return

        # we just reverse the number
        nums.reverse()