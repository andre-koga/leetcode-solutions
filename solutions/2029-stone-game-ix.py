# admittedly very bad
# i figured there was a way to simplify it and use only math instead of playing the game out
# but i didn't notice that they're forced to play the same type of remainder for the rest of the game
# aka A B A B A B A B A B ...
#     1 1 2 1 2 1 2 1 2 1 ...
# or  2 2 1 2 1 2 1 2 1 2 ...

# this is definitely the key to simplify everything

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        # alice only wins if she can force all of the remaining stones to have the same remainder mod 3; if there are at least two different remainders, then bob can always pick one of them s.t. the sum isn't divisible by 3.
        # note this is a prerequisite not an automatic win for her.
        # note the order of operations also doesn't matter for any pair of stones; if alice picks stone x then bob picks stone y and neither of them lose, then (x + y) % 3 == (y + x) % 3
        # we try to setup pairs of stones s.t. (x + y) % 3 == 0 so that whenever alice picks a stone in this pair, bob picks the other stone in the pair
        # since the sum never changes the remainder, and alice picks the first stone, the only exception is the first stone that bob picks
        
        zero, one, two = 0, 0, 0

        # all remainders
        for stone in stones:
            if stone % 3 == 0:
                zero += 1
            elif stone % 3 == 1:
                one += 1
            else:
                two += 1

        return self.attempt(zero, one, two, 1) or self.attempt(zero, one, two, 2)
        
        # i just noticed that since there are only 3 remainders this is kinda cyclical. every remainder is neighboring every other remainder. that's why the hint says to just do it greedily?

    def attempt(self, zero: int, one: int, two: int, firstOption: int) -> bool:
        # taking the first turn for alice automatically
        aliceTurn = False
        curr = 0

        if firstOption == 1:
            if not one:
                return False
            
            curr = 1
            one -= 1
        else:
            if not two:
                return False

            curr = 2
            two -= 1

        # greedy approach - take from the one with the biggest amount?
        while zero + one + two > 0:
            if curr == 1 and one:
                curr = 2
                one -= 1
            elif curr == 2 and two:
                curr = 1
                two -= 1
            elif curr == 1 and zero:
                curr = 1
                zero -= 1
            elif curr == 2 and zero:
                curr = 2
                zero -= 1
            else:
                return not aliceTurn

            aliceTurn = not aliceTurn

        # last turn was wrong
        if curr == 0:
            return aliceTurn

        return False
