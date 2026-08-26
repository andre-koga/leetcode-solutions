# i'm surprised this monstrosity actually works
# and it somehow is 0ms?
# i guess as bad as the code looks, it is still performant because we are just moving the two pointers forward
# they never reset, and we are just doing simple if else comparisons

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        lenS = len(s)
        l, r = 0, 0
        count = 0
        
        # will keep going until it finds enough 1s, r is inclusive
        while r < lenS and count < k:
            if s[r] == "1":
                count += 1
                if count == k:
                    break
                # break early so r doesn't add 1 again
            r += 1
        
        # no valid string found
        if count < k:
            return ""

        # now we move l until it stops at the first 1
        while s[l] != "1":
            l += 1

        # we know where to start checking all strings now
        bestLen = r - l + 1
        options = [s[l:r + 1]]

        # we now move r to the right until it finds another 1
        # then we move l to the right until it drops a 1, etc.
        while True:
            r += 1
            if r >= lenS:
                break

            while r < lenS and s[r] != "1":
                r += 1
            if r >= lenS:
                break

            # it'll go until it can drop a 1 and then drop as many zeroes
            # as possible
            while s[l] != "1":
                l += 1
            l += 1
            # jump all zeroes
            while s[l] == "0":
                l += 1

            # another valid option
            if r - l + 1 == bestLen:
                options.append(s[l:r + 1])
            elif r - l + 1 < bestLen:
                options = [s[l:r + 1]]
                bestLen = r - l + 1
                
        # finally got all options, just sort
        options.sort()
        return options[0]
