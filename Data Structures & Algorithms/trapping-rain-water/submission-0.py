class Solution:

    def trap(self, height: List[int]) -> int:
        waters = [0 for _ in range(len(height))]

        for i in range(len(height)):
            left = max(height[:i]) if height[:i] else 0
            right = max(height[i:]) if height[i:] else 0

            if left > height[i] and right > height[i]:
                waters[i] += min(left, right) - height[i]
        
        return sum(waters)


        