class Solution:
    def capitalizeTitle(self, title):
        words = title.split()
        result = []

        for w in words:
            if len(w) <= 2:
                result.append(w.lower())
            else:
                result.append(w[0].upper() + w[1:].lower())

        return " ".join(result)