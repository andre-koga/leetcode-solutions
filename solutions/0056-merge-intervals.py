# original solution, saw the "sorting" tag on the problem and immediately realized how
# to solve it lol

# beats 100% with 0ms runtime :O

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort first

        if len(intervals) <= 1:
            return intervals

        intervals = sorted(intervals, key = lambda x: x[0])

        result = [intervals[0]]

        for interval in intervals[1:]:
            if result[-1][-1] >= interval[0]:
                if result[-1][-1] < interval[1]:
                    result[-1] = [result[-1][0], interval[1]]
            else:
                result.append(interval)

        return result