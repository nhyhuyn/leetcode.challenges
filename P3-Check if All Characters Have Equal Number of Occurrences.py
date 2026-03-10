class Solution:
    def areOccurrencesEqual(self, s):
        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1

        freq = list(count.values())
        return len(set(freq)) == 1