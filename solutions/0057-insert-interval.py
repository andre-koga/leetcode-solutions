# original solution inspired on the previous problem 56
# also beats 100%

# time complexity: O(N + logN) = O(N) (though faster than linear search)
# space complexity is N 

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)

        if n == 0:
            return [newInterval]
        
        # divide and conquer to find the position of the newStart
        # then do the same thing as the last problem

        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if intervals[m][0] < newInterval[0]:
                l = m + 1
            else:
                r = m - 1

        intervals.insert(l, newInterval)

        # to avoid an empty results list
        if m == 0:
            m = 1
        
        result = intervals[0:m]

        for interval in intervals[m:]:
            if result[-1][-1] >= interval[0]:
                if result[-1][-1] < interval[1]:
                    result[-1] = [result[-1][0], interval[1]]
            else:
                result.append(interval)
            
        return result
        