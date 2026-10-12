class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        # the real question is: how do we figure out what is the max value we can get?
        # we call a "redundancy" when there's a 1 for both nums[i][X] and nums[j][X]

        # AND only works when both have 1s => there's a 1 after the AND operation if there's a redundancy on digit X
        # OR only loses efficiency when there's redundancy, which is when AND works; so we can conclude that OR and AND preserve the number of redundancies between numbers nums[i] and nums[j]
        #          AND    OR
        # example: 100110 100110
        # and      011011 011011
        #          000010 111121
        # note the only redundancy on OR ends up on the AND final result
        
        # what does this mean? it means that the number after the OR operation always accumulates more and more 1s, and the number on the AND operation always transfers its 1s; the operations are invariant and lossless, so we don't need to worry about making bad operations.
        # this means we can greedily slowly transfer the 1s to a single number, let's say nums[0],
        # until it gets as many 1s as we can. then we repeat the process to number nums[1], etc.
        # until we fill out all of the possible 1s on the first k numbers in nums. this can be done
        # without fail, and we don't need to think about the operations, the final result is the same.

        # so we just need to count how many 1s we got on each position that could be transferred to the first k numbers in the array, square the first k numbers after that, and add (then module 10^9 + 7)

        # k can be gigantic, we need to think of an efficient way to figure the 1s. is doing the actual AND / OR operations the cheapest way?

        # n = len(nums)
        # maxNum = 0

        # for i in range(n):
        #     if nums[i] > maxNum:
        #             maxNum = nums[i] # figure out the biggest leading 1 so we speed up

        # maxFullNum = 1
        # while maxFullNum <= maxNum:
        #     maxFullNum *= 2
        
        # maxFullNum -= 1

        # for i in range(k):
        #     for j in range(i + 1, n):
        #         if nums[i] == 0 or nums[j] == 0: # zeroes are meaningless
        #             continue
                
        #         nums[i], nums[j] = nums[i] | nums[j], nums[i] & nums[j]
        #         print(nums)

        #         if nums[i] == maxFullNum:
        #             break

        # print(nums)

        # return sum([x * x for x in nums[:k]])

        # correct but too slow

        n = len(nums)

        bits = [0] * 30
        
        for num in nums:
            bit = 0
            while num > 0:
                if num & 1:
                    bits[bit] += 1
                num >>= 1
                bit += 1

        # now we get the squares and stuff
        finalNums = [0] * k
        for i in range(k):
            for j in range(30):
                if bits[j] > 0:
                    finalNums[i] |= 1 << j
                    bits[j] -= 1
        
        return sum(x * x for x in finalNums) % 1_000_000_007
