class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        count = {}
        
        # Tính tổng của nums1 và nums2
        for a in nums1:
            for b in nums2:
                s = a + b
                count[s] = count.get(s, 0) + 1
        
        result = 0
        
        # Kiểm tra nums3 và nums4
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in count:
                    result += count[target]
        
        return result