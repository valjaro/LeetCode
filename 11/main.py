class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        while left != right:
            width = right - left
            area = min(height[left], height[right]) * width
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

if __name__ == "__main__":
    s = Solution()
    height = [1,2,4,3]
    r = s.maxArea(height)
    print(r)