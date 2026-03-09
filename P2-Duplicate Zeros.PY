class Solution:
    def duplicateZeros(self, arr):
        i = 0
        n = len(arr)

        while i < n:
            if arr[i] == 0:
                arr.insert(i, 0)  # duplicate zero
                arr.pop()         # keep array size same
                i += 1            # skip the duplicated zero
            i += 1