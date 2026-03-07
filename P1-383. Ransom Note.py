class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = {}

        # Đếm số lần xuất hiện của từng chữ trong magazine
        for char in magazine:
            count[char] = count.get(char, 0) + 1

        # Kiểm tra từng chữ trong ransomNote
        for char in ransomNote:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1

        return True