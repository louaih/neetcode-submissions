class Solution:
    def calcArea(self, leftVal, leftInd, rightVal, rightInd):
        return max(min(leftVal, rightVal) * (rightInd - leftInd), min(leftVal, rightVal) * (leftInd - rightInd))
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        waters = []
        
        while left < right:
            a = self.calcArea(heights[left], left, heights[right], right)
            waters.append(a)

            if (heights[left] > heights[right]):
                right -= 1
            else:
                left += 1

        
        return max(waters)

        