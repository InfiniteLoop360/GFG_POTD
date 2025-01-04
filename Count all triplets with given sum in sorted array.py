class Solution:
    def countTriplets(self, arr, target):
        n = len(arr)
        count = 0
        
        # Traverse the array for the first element
        for i in range(n - 2):
            # Initialize two pointers
            j, k = i + 1, n - 1
            
            while j < k:
                current_sum = arr[i] + arr[j] + arr[k]
                
                if current_sum == target:
                    # Calculate combinations for duplicates
                    if arr[j] == arr[k]:
                        # If all elements between j and k are the same
                        count += (k - j + 1) * (k - j) // 2
                        break
                    else:
                        # Count duplicates for j and k separately
                        left_count, right_count = 1, 1
                        while j + 1 < k and arr[j] == arr[j + 1]:
                            j += 1
                            left_count += 1
                        while k - 1 > j and arr[k] == arr[k - 1]:
                            k -= 1
                            right_count += 1
                        
                        count += left_count * right_count
                        j += 1
                        k -= 1
                elif current_sum < target:
                    j += 1
                else:
                    k -= 1
        
        return count
