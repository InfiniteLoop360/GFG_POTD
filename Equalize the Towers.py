class Solution:
    def minCost(self, heights, cost):
        def get_total_cost(target_height):
            return sum(abs(h - target_height) * c for h, c in zip(heights, cost))

        low, high = min(heights), max(heights)
        answer = float('inf')

        while low <= high:
            mid = (low + high) // 2
            cost1 = get_total_cost(mid)
            cost2 = get_total_cost(mid + 1)

            answer = min(answer, cost1, cost2)

            if cost1 < cost2:
                high = mid - 1
            else:
                low = mid + 1

        return answer
