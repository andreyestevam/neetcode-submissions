# Write solution here!
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(height)-1
        while l < r:
            minHeight = min(height[l], height[r])
            width = r - l
            currArea = minHeight * width
            if currArea > maxArea:
                maxArea = currArea
            if height[l] < height[r]: # Means left was the constraint
                l += 1
            elif height[l] > height[r]: # Can condense this into the else and then just r -= 1
                r -= 1
            else:
                l += 1
                r -= 1
        
        return maxArea