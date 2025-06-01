class Solution:
    def countPairs(self, mat1, mat2, x):
        n = len(mat1)
        # Flatten both matrices
        list1 = [mat1[i][j] for i in range(n) for j in range(n)]
        list2 = [mat2[i][j] for i in range(n) for j in range(n)]

        # Store frequency of elements in mat2
        freq = {}
        for num in list2:
            freq[num] = freq.get(num, 0) + 1

        count = 0
        for a in list1:
            target = x - a
            if target in freq:
                count += freq[target]

        return count
