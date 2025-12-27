class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        """
        # are all of the words inside s also of same length? yes
        # words aren't necessarily unique... bruh
        # brute force

        result = []
        size = len(words[0])
        words_len = len(words)

        for i in range(len(words[0])):
            result += self.solver(s, words, size, words_len, i)

        return result

    def solver(self, s, words, size, words_len, start_l):
        answer = []
        seen = []
        _words = words[:]
        l = start_l

        while l < len(s):
            maybe = s[l : l + size]
            if maybe not in words:
                # easy case - clean up, go forward
                seen = []
                _words = words[:]
                l += size
            else:
                maybe_index = words.index(maybe)
                if maybe_index not in seen:
                    # easy case - add word, check if won, go forward
                    seen.append(maybe_index)
                    _words.remove(maybe)
                    l += size
                    if len(seen) == words_len:
                        answer.append(l - size * words_len)
                else:
                    # the word is a duplicate. if not in _words,
                    # we remove all words before the first duplicate (inclusive), append the new one,
                    # check if won, then go forward. if inside _words,
                    # we remove it from _words, and it might still be a success.
                    # we also need to smartly change _words
                    if maybe not in _words:
                        first_seen = seen.index(maybe_index)
                        seen = seen[first_seen + 1 :]
                        seen.append(maybe_index)
                        _words = words[:]
                        for word_index in seen:
                            _words.remove(words[word_index])
                        l += size
                        if len(seen) == words_len:
                            answer.append(l - size * words_len)
                    else:
                        # despite being a duplicate, the words list has multiple too, so everything is fine
                        seen.append(maybe_index)
                        _words.remove(maybe)
                        l += size
                        if len(seen) == words_len:
                            answer.append(l - size * words_len)
        return answer
        """
        # time complexity: O(word_size * string_size), since we are going through the entire string
        # for each starting index

        # space complexity: O(word_size * words_length), since worst case scenario each word
        # shows up once inside our hashmap

        # now we try to optimize
        hash_words = {}
        for word in words:
            if word not in hash_words:
                hash_words[word] = 1
            else:
                hash_words[word] = hash_words[word] + 1
        # now we have a list of unique words, each with a number indicating how often that word shows up

        result = []
        size = len(words[0])
        words_len = len(words)

        for i in range(size):
            result += self.solver(s, hash_words, i, size)

        return result

    def solver(self, s, hash_words, l, size):
        result = []
        s_len = len(s)
        _hash_words = {}
        r = l

        while r < s_len:
            word = s[r : r + size]
            r += size

            if word not in hash_words:
                _hash_words = {}
                l = r
            else:
                if word in _hash_words:
                    _hash_words[word] += 1
                else:
                    _hash_words[word] = 1

                while _hash_words[word] > hash_words[word]:
                    removed_word = s[l : l + size]
                    l += size
                    _hash_words[removed_word] -= 1
                    
            if hash_words == _hash_words:
                result.append(l)

        return result
