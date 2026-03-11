class Solution:
    def checkValid(self, matrix):
        n = len(matrix)

        for i in range(n):
            if set(matrix[i]) != set(range(1, n+1)):
                return False
            
            column = [matrix[j][i] for j in range(n)]
            if set(column) != set(range(1, n+1)):
                return False

        return True