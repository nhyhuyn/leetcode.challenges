class Solution:
    def countHillValley(self, nums):
        arr = [nums[0]]
        
        # bỏ các số trùng nhau liên tiếp
        for num in nums:
            if num != arr[-1]:
                arr.append(num)
        
        count = 0
        
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                count += 1
            elif arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                count += 1
        
        return count