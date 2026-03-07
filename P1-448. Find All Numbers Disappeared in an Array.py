class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = []

        # Đánh dấu các số đã xuất hiện
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        # Những vị trí còn số dương là số chưa xuất hiện
        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)

        return result