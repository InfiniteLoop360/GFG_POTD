class Solution:
    def uniquePerms(self, arr):
        arr.sort()   # Step 1: sort for lexicographic order + easier duplicate handling
        result = []
        used = [False] * len(arr)

        def backtrack(path):
            if len(path) == len(arr):
                result.append(path[:])  
                return

            for i in range(len(arr)):
                if used[i]:
                    continue

                if i > 0 and arr[i] == arr[i-1] and not used[i-1]:
                    continue

                used[i] = True
                path.append(arr[i])

                backtrack(path)

                path.pop()
                used[i] = False

        backtrack([])
        return result
