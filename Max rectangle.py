class Solution:
    def maxArea(self, mat):
        if not mat or not mat[0]:
            return 0

        n, m = len(mat), len(mat[0])
        heights = [0] * m
        max_area = 0

        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            heights.append(0)  # sentinel
            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
            heights.pop()  # remove sentinel
            return max_area

        for r in range(n):
            for c in range(m):
                if mat[r][c] == 1:
                    heights[c] += 1
                else:
                    heights[c] = 0
            max_area = max(max_area, largestRectangleArea(heights))

        return max_area
