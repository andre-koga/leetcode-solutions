class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        n = len(arr1)
        
        for x in arr1:
            for y in arr2:
                if abs(x - y) <= d:
                    n -= 1
                    break

        return n
