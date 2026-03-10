class Solution:
    def maxDistance(self, colors):
        n = len(colors)
        max_dist = 0

        for i in range(n):
            for j in range(n-1, -1, -1):
                if colors[i] != colors[j]:
                    max_dist = max(max_dist, abs(i - j))
                    break

        return max_dist