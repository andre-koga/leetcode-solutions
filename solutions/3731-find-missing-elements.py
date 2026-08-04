class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # lazy would be 2n: first run to find smallest and largest
        # second run to remove all that show up
        # also this is an easy level problem, so prob the lazy system is enough

        currSmallest = nums[0]
        currLargest = nums[0]

        for number in nums:
            if number < currSmallest:
                # we found a new smallest number
                currSmallest = number
            elif number > currLargest:
                # we found a new biggest number
                currLargest = number
        
        missingArray = []
        for i in range(currSmallest + 1, currLargest):
            if i not in nums:
                missingArray.append(i)

        return missingArray

        # the boolean array method is very simple and clever, and solves
        # it in O(n), much better
