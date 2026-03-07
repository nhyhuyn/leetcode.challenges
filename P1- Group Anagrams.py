class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}

        for word in strs:
            # Sắp xếp chữ cái để tạo key
            key = "".join(sorted(word))

            if key not in hashmap:
                hashmap[key] = []

            hashmap[key].append(word)

        return list(hashmap.values())