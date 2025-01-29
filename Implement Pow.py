class Solution:
    def power(self, b: float, e: int) -> float:
        if e == 0:
            return 1.0  # Any number raised to power 0 is 1
        
        # Handle negative exponent
        if e < 0:
            b = 1 / b
            e = -e
        
        result = 1.0
        while e:
            if e % 2 == 1:  # If exponent is odd
                result *= b
            b *= b  # Square the base
            e //= 2  # Reduce exponent by half
        
        return round(result, 5)  # Round to match precision constraints
