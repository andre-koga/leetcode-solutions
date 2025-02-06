# one of my most clever solutions, completely original as well!
# better than 99% of submissions speed wise! it loses to pretty much everybody when
# it comes to memory though, but honestly who cares. speed is way more important.

# we basically keep track of possible options, keep iterating through them and discarding the
# invalid ones.

# when we reach valid results we just append them into the results array


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

        # some quick cases
        if n == 1:
            if target % candidates[0] != 0:
                return []
            else:
                return [candidates] * (target // candidates)

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
        # most recently added candidate to the array. for that we use i, the index of the
        # most recent candidate
        
        # options[i] = (current possible result, newTarget, index of latest candidate)

        options = []
        result = []
        for i in range(n):
            options.append(([candidates[i]], target - candidates[i], i))

        while len(options) != 0:
            for i in range(len(options)):
                option = options.pop(0)
                if option[1] == 0:
                    # found a valid one!
                    result.append(option[0])
                elif option[1] >= option[0][-1]:
                    # keep on going
                    for j in range(option[2], n):
                        if candidates[j] > option[1]:
                            break
                        options.append((option[0] + [candidates[j]], option[1] - candidates[j], j))

        return result