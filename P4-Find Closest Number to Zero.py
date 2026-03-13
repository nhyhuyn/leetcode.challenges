class Solution:
    def findClosestNumber(self, nums):
        result = nums[0]

        for num in nums:
            if abs(num) < abs(result):
                result = num
            elif abs(num) == abs(result) and num > result:
                result = num

        return result