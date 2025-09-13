class Solution:
    def minCost(self, n, m, x, y):
        """
        n: number of rows (vertical count)
        m: number of columns (horizontal count)
        x: list of length m-1 -> vertical cut costs
        y: list of length n-1 -> horizontal cut costs

        Returns minimum total cost to cut the board into n*m squares.
        """
        # Sort both cost arrays in descending order
        x_sorted = sorted(x, reverse=True)
        y_sorted = sorted(y, reverse=True)

        i = 0  # pointer in x_sorted (vertical cuts)
        j = 0  # pointer in y_sorted (horizontal cuts)

        horizontal_pieces = 1
        vertical_pieces = 1

        total_cost = 0

        # While both arrays have remaining cuts
        while i < len(x_sorted) and j < len(y_sorted):
            if x_sorted[i] >= y_sorted[j]:
                # take vertical cut
                total_cost += x_sorted[i] * horizontal_pieces
                vertical_pieces += 1
                i += 1
            else:
                # take horizontal cut
                total_cost += y_sorted[j] * vertical_pieces
                horizontal_pieces += 1
                j += 1

        # Process remaining vertical cuts (if any)
        while i < len(x_sorted):
            total_cost += x_sorted[i] * horizontal_pieces
            vertical_pieces += 1
            i += 1

        # Process remaining horizontal cuts (if any)
        while j < len(y_sorted):
            total_cost += y_sorted[j] * vertical_pieces
            horizontal_pieces += 1
            j += 1

        return total_cost
