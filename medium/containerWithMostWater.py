class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0

        while right - left > 0:
            result = max(result, (right - left) * min(height[left], height[right]))

            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1

        return result
