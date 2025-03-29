class Solution:
    def jobSequencing(self, deadline, profit):
        jobs = list(zip(deadline, profit))
        jobs.sort(key=lambda x: -x[1])  # Sort by profit in descending order
        
        max_deadline = max(deadline)  # Find max deadline
        parent = list(range(max_deadline + 1))  # Union-Find parent array
        
        def find(slot):  # Disjoint Set Find operation
            if parent[slot] == slot:
                return slot
            parent[slot] = find(parent[slot])  # Path compression
            return parent[slot]
        
        def union(slot1, slot2):  # Union operation
            parent[slot1] = slot2
        
        job_count = 0
        total_profit = 0

        for d, p in jobs:
            available_slot = find(min(d, max_deadline))  # Find latest available slot before deadline
            
            if available_slot > 0:  # If a slot is available
                union(available_slot, available_slot - 1)  # Mark the slot as used
                job_count += 1
                total_profit += p

        return [job_count, total_profit]
