from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s):
        count = Counter(s)
        freq = list(count.values())
        
        return len(set(freq)) == 1