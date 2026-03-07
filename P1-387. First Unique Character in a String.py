class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}

        # Đếm số lần xuất hiện của mỗi ký tự
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Tìm ký tự đầu tiên xuất hiện đúng 1 lần
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1