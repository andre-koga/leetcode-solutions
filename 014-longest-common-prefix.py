class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        index = 0
        while index < len(strs[0]):
            for i, string in enumerate(strs):
                if i == 0:
                    continue
                elif len(string) <= index or string[index] != strs[0][index]:
                    return strs[0][0:index]
            index += 1

        return strs[0]