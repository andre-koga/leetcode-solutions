class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # time complexity: O(N) because we checking the whole string linearly with
        # just a bunch of conditions
        # space complexity: O(N) because we are storing inside islands valid candidates
        # that grow in size as s grows.
        
        # let's try dp
        islands = []

        i = 1 # we start at 1 because no point in checking the 0th
        n = len(s)

        if n <= 1:
            return 0

        while i < n:
            if s[i] == "(":
                i += 1
                continue
            
            # only ")" cases
            if s[i - 1] == "(":
                if len(islands) == 0:
                    islands.append([i - 1, i])
                # simple case - check if annex or not
                elif islands[-1][1] == i - 2:
                    # annex! +2
                    islands[-1][1] = i
                else:
                    # new island
                    islands.append([i - 1, i])
            elif len(islands) > 0 and islands[-1][0] > 0:
                # complex case - could lead to a domino effect
                # in which the two previous islands connect
                # ()(()')' for example
                if s[islands[-1][0] - 1] == ")":
                    i += 1
                    continue

                # expand this island! check if annex with previous
                if len(islands) > 1 and islands[-2][1] == islands[-1][0] - 2:
                    # annex!
                    islands.pop()
                    islands[-1][1] = i
                else:
                    # nothing to annex. just expand both ways
                    islands[-1][0] -= 1
                    islands[-1][1] += 1

            # and go to next index
            i += 1

        best = 0
        for island in islands:
            if island[1] - island[0] + 1 > best:
                best = island[1] - island[0] + 1

        return best
        
