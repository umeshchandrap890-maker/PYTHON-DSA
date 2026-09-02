class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)

        total = n * (n + 1) // 2

        arr_sum = sum(nums)

        missing = total - arr_sum

        return missing