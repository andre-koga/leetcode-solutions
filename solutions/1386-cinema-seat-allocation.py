import collections

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # seats 1 and 10 are meaningless
        # seats 2 & 3 / 8 & 9 lead to the same implications
        # seats 4 & 5 / 6 & 7 lead to the same implications
        # we can only have 2 groups in a single row if we have it empty (ignore 1 and 10)
        # if we have only a single seat reserved in a single row it automatically must exactly
        # fit one group (ignore 1 and 10)

        # binary
        # 1 2 3 4 5  6  7  8
        # 0 1 2 3 4  5  6  7  
        # 1 2 4 8 16 32 64 128
        # left side mask is 1 + 2 + 4 + 8 = 15
        # right side mask is 16 + 32 + 64 + 128 = 240
        # middle mask is 4 + 8 + 16 + 32 = 60

        # figured it out by myself, ran out of memory, then checked online how to
        # get a more efficient hashmap, boom done!
        
        encoding = collections.defaultdict(int)

        for seat in reservedSeats:
            if seat[1] == 1 or seat[1] == 10:
                continue
            
            encoding[seat[0] - 1] |= 1 << (seat[1] - 2)


        total = (n - len(encoding)) * 2
        for code in encoding.values():
            if code == 0:
                total += 2
            elif code & 15 == 0 or code & 240 == 0 or code & 60 == 0:
                total += 1
            
        return total
