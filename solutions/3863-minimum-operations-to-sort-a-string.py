# lazy solution, in which i use the sortedS.sort(), but
# if you want to be more efficient you can define maxC and minC and do a for loop

class Solution:
    def minOperations(self, s: str) -> int:
        size = len(s)
        listS, sortedS = list(s), list(s)
        sortedS.sort()

        # print(listS, sortedS)

        if size == 1 or sortedS == listS:
            return 0
        elif size == 2:
            return -1
        elif listS[0] == sortedS[0] or listS[-1] == sortedS[-1]:
            return 1
        elif listS[0] == sortedS[-1] and listS[0] != sortedS[-2] and listS[-1] == sortedS[0] and listS[-1] != sortedS[1]:
            return 3
        else:
            return 2
