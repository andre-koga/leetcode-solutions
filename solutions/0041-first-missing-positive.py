# not an original solution. read the first few lines of someone else's solution and then implemented it myself
# i didn't think of first removing the negative numbers so we can use negatives as information!

# beats 60%, follows the space and time constraints

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # without space constraint:
        # we create a notShownYet list
        # that has the range from 1 to n + 1
        # we would perform a for loop
        # and for every number we check,
        # we remove that number from the notShownYet
        # then we return the first item still remaining from the list
        
        # space: O(n) because of the external list
        # time: O(2n) = O(n)

        # but we want to do this with O(1) auxiliary space
        # therefore, we must do the same thing without using an external list
        # how?

        # we remove the non-positive numbers first!

        nums = [n for n in nums if n > 0]
        size = len(nums)

        # now we use negative as information

        for n in nums:
            index = abs(n) - 1 # we use absolute bc it might alr be flipped!
            if index < size and nums[index] > 0:
                nums[index] = -nums[index]
        

        # the first positive index must not have shown up!

        for i in range(size):
            if nums[i] > 0:
                return i + 1
        
        return size + 1 # we return this because all numbers have shown up!