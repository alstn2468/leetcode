class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c = [0 for _ in range(len(nums))]
        c[0] = nums[0]

        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            c[i] = max(0, c[i - 1]) + nums[i]
        return max(c)
