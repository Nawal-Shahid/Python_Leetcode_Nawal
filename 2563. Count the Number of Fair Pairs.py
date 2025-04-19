class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        def lower_bound(arr, target, start):
            left, right = start, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        def upper_bound(arr, target, start):
            left, right = start, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n):
            min_val = lower - nums[i]
            max_val = upper - nums[i]

            left = lower_bound(nums, min_val, i + 1)
            right = upper_bound(nums, max_val, i + 1)

            count += right - left

        return count
