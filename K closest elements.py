from bisect import bisect_left

class Solution:
    def printKClosest(self, arr, k, x):
        n = len(arr)
        index = bisect_left(arr, x)  # Find position to insert x

        left = index - 1
        right = index

        # If x exists in arr, skip it
        if right < n and arr[right] == x:
            right += 1

        result = []

        while k > 0:
            if left >= 0 and right < n:
                dist_left = abs(arr[left] - x)
                dist_right = abs(arr[right] - x)

                if dist_left < dist_right:
                    result.append(arr[left])
                    left -= 1
                elif dist_left > dist_right:
                    result.append(arr[right])
                    right += 1
                else:
                    # Equal distance: prefer larger element
                    if arr[left] > arr[right]:
                        result.append(arr[left])
                        left -= 1
                    else:
                        result.append(arr[right])
                        right += 1
            elif left >= 0:
                result.append(arr[left])
                left -= 1
            elif right < n:
                result.append(arr[right])
                right += 1
            else:
                break
            k -= 1

        return result
