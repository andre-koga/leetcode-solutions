# better than 99% of submissions for time!

# check solution for problem 39 - combination sum. I did basically the same thing,
# with just some little adjustments due to the differences of the prompt.

# the logic itself hasn't changed.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

        # some quick cases
        if n == 1:
            if target != candidates[0]:
                return []
            else:
                return [candidates]

        candidates.sort()
        if target < candidates[0]:
            return []
        elif target < candidates[-1]:
            # lets trim the list to ensure efficiency
            cutAt = 0
            while candidates[cutAt] <= target:
                cutAt += 1
            del candidates[cutAt:]
            n = len(candidates)

        # we set a new target equal to target - candidates[i], for all valid i. then we
        # repeat. keep track of our operations by putting stuff in a temporary list.
        # if we reach candidates[i] == newTarget, then it is a valid
        # option. if we reach candidates[0] > newTarget, then it is invalid.

        # to avoid duplicates we only look for new candidates equal to or bigger than our
        # most recently added candidate to the array
        
        options = [([candidates[0]], target - candidates[0], 0)]
        result = set()
        latest = candidates[0]
        for i in range(1, n):
            if latest != candidates[i]:
                latest = candidates[i]
                options.append(([candidates[i]], target - candidates[i], i))

        while len(options) != 0:
            for i in range(len(options)):
                option = options.pop(0)
                if option[1] == 0:
                    # found a valid one!
                    result.add(tuple(option[0]))
                elif option[1] >= option[0][-1]:
                    # keep on going
                    k = option[2] + 1
                    if k < n:
                        options.append((option[0] + [candidates[k]], option[1] - candidates[k], k))
                        latest = candidates[k]
                    for j in range(option[2] + 2, n):
                        if candidates[j] > option[1]:
                            break
                        if latest != candidates[j]:
                            latest = candidates[j]
                            options.append((option[0] + [candidates[j]], option[1] - candidates[j], j))

        return result