# definitely not the most efficient solution since it only uses
# brute force. for anything more efficient there are multiple
# well known algorithms out there such as Rabin-Karp, KMP, and
# Boyer-Moore.

# i simply used the pointer solution.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        while left <= len(haystack) - len(needle):
            right, pointer = 0, 0
            while haystack[left + pointer] == needle[right]:
                pointer += 1
                right += 1
                if right == len(needle):
                    return left
            left += 1
        return -1