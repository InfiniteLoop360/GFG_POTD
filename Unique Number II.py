class Solution:
    def singleNum(self, arr):
        # Step 1: XOR all elements to get x^y, where x and y are the two uniques
        x_xor_y = 0
        for num in arr:
            x_xor_y ^= num

        # Step 2: Find a bit that’s set in x_xor_y (rightmost set bit)
        # This bit differs between x and y
        mask = x_xor_y & -x_xor_y

        # Step 3: Partition the numbers into two groups based on that bit,
        #         and XOR within each group to isolate x and y
        x = 0
        y = 0
        for num in arr:
            if num & mask:
                x ^= num
            else:
                y ^= num

        # Step 4: Return the two uniques in increasing order
        return [x, y] if x < y else [y, x]
