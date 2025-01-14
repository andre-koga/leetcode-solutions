# semi original; saw some hints because despite knowing that the solution required two pointers, i
# didn't have the realization that the water on the current index can simply be calculated according to the min of the two bests
# beats 99% at 1ms, it is O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        # what math operation are we really doing here?

        length = len(height)

        if length <= 2:
            return 0

        # use two pointers to track from left and right
        
        l, r = 0, length - 1
        bestLeft, bestRight = height[l], height[r]
        water = 0

        while l < r:
            if bestLeft <= bestRight:
                l += 1
                if height[l] > bestLeft:
                    bestLeft = height[l]
                else:
                    water += bestLeft - height[l]
            else:
                r -= 1
                if height[r] > bestRight:
                    bestRight = height[r]
                else:
                    water += bestRight - height[r]

        return water