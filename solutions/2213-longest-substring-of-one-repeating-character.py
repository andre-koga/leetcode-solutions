class Solution:
    A = []
    ST = []

    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        # first intuition: keep a list that will contain all of the longest substrings of one repeating character.
        # we do the first pass before any operation
        # then after every operation, we check this list to see what has changed
        # meaning we always can easily just check this list to see the longest sequence
        # the question becomes: i want to quickly check this list, and i need to be able to search for the longest range, and also search based on the index.
        # my initial intuition was to have an array with tuples that indicated the beginning and end of a sequence
        # [(l1, r1), (l2, r2), ...]
        # this isn't good for searching or ordering
        # at the same time, i usually get stuck and confused when i overcomplicate things, so i should probably just try the naive version first and then improve it over time

        k = len(queryCharacters)
        lenS = len(s)

        # naive case
        if lenS == 1:
            return [1] * k

        # ok so i tried the naive version, and realized
        # it is very clunky and requires a bunch of nested if statements
        # checking the hint 1 says i can use a segment tree (which i didn't know about)
        # so i searched on geeksforgeeks and now i think i can use it

        self.A = s
        self.ST = [0 for _ in range(4 * lenS)]
        self.build(0, 0, lenS - 1)

        result = []
        for i in range(k):
            self.update(0, 0, lenS - 1, queryIndices[i], queryCharacters[i])
            result.append(self.ST[0][0])

        return result

    def build(self, node: int, l: int, r: int):
        # leaf
        if l == r:
            # tuple with the length of the best seq, the prefix, the prefix char, the suffix, the suffix char, and the size
            self.ST[node] = (1, 1, self.A[l], 1, self.A[r], 1)
        else:
            # split in half and recurse
            mid = (l + r) // 2

            self.build(node * 2 + 1, l, mid)
            self.build(node * 2 + 2, mid + 1, r)

            # finally we get the value required for the parent
            # what is this value? the longest sequence in this range surely
            # we just need to check if there's a even longer sequence formed
            # when we merge the two sides, which is easy

            leftNode, rightNode = self.ST[node * 2 + 1], self.ST[node * 2 + 2]
            
            pre = leftNode[1]
            if leftNode[1] == leftNode[5] and leftNode[2] == rightNode[2]:
                # this prefix increased!
                pre = leftNode[1] + rightNode[1]
            suf = rightNode[3]
            if rightNode[3] == rightNode[5] and leftNode[4] == rightNode[4]:
                # this suffix increased!
                suf = rightNode[3] + leftNode[3]

            merged = 0
            if leftNode[4] == rightNode[2]:
                # left node and right node can merge!
                merged = leftNode[3] + rightNode[1]

            self.ST[node] = (max(leftNode[0], rightNode[0], merged), pre, leftNode[2], suf, rightNode[4], leftNode[5] + rightNode[5])

    def update(self, node, l, r, idx, newChar):
        if l == r:
            # this is the root node to update
            self.ST[node] = (1, 1, newChar, 1, newChar, 1)
        else:
            mid = (l + r) // 2

            if l <= idx and idx <= mid:
                self.update(2 * node + 1, l, mid, idx, newChar)
            else:
                self.update(2 * node + 2, mid + 1, r, idx, newChar)

            # then we update the parent

            leftNode, rightNode = self.ST[node * 2 + 1], self.ST[node * 2 + 2]
            
            pre = leftNode[1]
            if leftNode[1] == leftNode[5] and leftNode[2] == rightNode[2]:
                # this prefix increased!
                pre = leftNode[1] + rightNode[1]
            suf = rightNode[3]
            if rightNode[3] == rightNode[5] and leftNode[4] == rightNode[4]:
                # this suffix increased!
                suf = rightNode[3] + leftNode[3]

            merged = 0
            if leftNode[4] == rightNode[2]:
                # left node and right node can merge!
                merged = leftNode[3] + rightNode[1]

            self.ST[node] = (max(leftNode[0], rightNode[0], merged), pre, leftNode[2], suf, rightNode[4], leftNode[5] + rightNode[5])
