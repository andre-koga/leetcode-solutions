class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # maybe useful observations:
        # the 1st pile will always go to Ana
        # the 4th pile, if optimal, will always go to Bob?
        # actually not true...

        # is this dynamic programming?
        # any list with 3 items only will always lead Alice to win?

        # obviously we can't brute force by testing every combination. Alice has 3 options, Bob has 3, etc. It grows exponentially. How do we remove the bad options? Are there any invariants? Are the best options for the first X stones the same as the best options for the first X + K stones? Does it change if we add more stones to the end of the list?
        # the end of the list does change the scenario: if we have [1,2,3,7], Alice always loses and her optimal choice is the first 3 stones. If we have [1,2,3,7,99], then it is best that she picks only the first stone 1. Then Bob, whatever he does, will leave the 99 for her, so she wins.
        # in this scenario, we can add any two stones after 99

        # had a hint: it needs to be run backwards
        dp = [0] * len(stoneValue)
        dp[-1] = stoneValue[-1]

        # manually do the first 3 so we can do the rest automatically
        if len(stoneValue) > 1:
            dp[-2] = max(stoneValue[-2] - dp[-1], stoneValue[-2] + stoneValue[-1])
        if len(stoneValue) > 2:
            dp[-3] = max(stoneValue[-3] - dp[-2], stoneValue[-3] + stoneValue[-2] - dp[-1], stoneValue[-3] + stoneValue[-2] + stoneValue[-1])


        for i in range(2, len(stoneValue) + 1):
            pickOne = stoneValue[-i] - dp[-i + 1]
            pickTwo = stoneValue[-i] + stoneValue[-i + 1] - dp[-i + 2]
            pickThree = stoneValue[-i] + stoneValue[-i + 1] + stoneValue[-i + 2] - dp[-i + 3]

            dp[-i] = max(pickOne, pickTwo, pickThree)

        if dp[0] == 0:
            return "Tie"
        elif dp[0] > 0:
            return "Alice"
        else:
            return "Bob"
