class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        
        # Đếm số lần xuất hiện
        count = Counter(nums)
        
        # Lấy k phần tử xuất hiện nhiều nhất
        return [item for item, freq in count.most_common(k)]