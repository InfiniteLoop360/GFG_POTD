class Solution:
    def maxKPower(self, n, k):
        # Function to factorize k into its prime factors
        def prime_factors(k):
            i = 2
            factors = {}
            while i * i <= k:
                while k % i == 0:
                    factors[i] = factors.get(i, 0) + 1
                    k //= i
                i += 1
            if k > 1:
                factors[k] = factors.get(k, 0) + 1
            return factors
        
        # Function to count how many times prime p appears in n!
        def count_p_in_factorial(n, p):
            count = 0
            power = p
            while power <= n:
                count += n // power
                power *= p
            return count

        factors = prime_factors(k)
        min_power = float('inf')

        for p in factors:
            power_in_fact = count_p_in_factorial(n, p)
            min_power = min(min_power, power_in_fact // factors[p])

        return min_power
