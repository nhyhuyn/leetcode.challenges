class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        prefix = strs[0]  # lấy chuỗi đầu tiên làm chuẩn
        
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # cắt bớt 1 ký tự cuối
                if not prefix:
                    return ""
        
        return prefix