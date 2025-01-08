# binary search bonanza! this is my original solution for the problem 34 of leetcode

# basically we search for a single instance of the target at index m with pointers l : r
# then we do two more searches with the pointers l : ll and rr : r
# (ll, rr = m, m)

# nothing crazy, just doing a bunch of if, elses to check different cases
# pretty efficient bc of that tho! better than 60% of ppl

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # first find a single item == target, then search for its border
        n = len(nums)

        if n == 0:
            return [-1, -1]

        l, r = 0, n - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                # search for boundaries. do two more binary searches
                # with the pointers [l, m] and [m, r]
                result = [-1, -1]
                ll, rr = m, m
                while l <= ll:
                    lm = (l + ll) // 2
            
                    if nums[lm] == target:
                        if lm == 0 or nums[lm - 1] != target:
                            result[0] = lm
                            break
                        # keep going to the left
                        ll = lm - 1
                    else:
                        if nums[lm + 1] == target:
                            result[0] = lm + 1
                            break
                        # too far, back to the right
                        l = lm + 1
                while rr <= r:
                    rm = (r + rr) // 2

                    if nums[rm] == target:
                        if rm == n - 1 or nums[rm + 1] != target:
                            result[1] = rm
                            break

                        # keep going to the right
                        rr = rm + 1
                    else:
                        if nums[rm - 1] == target:
                            result[1] = rm - 1
                            break

                        # too far
                        r = rm - 1
                return result
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return [-1, -1]