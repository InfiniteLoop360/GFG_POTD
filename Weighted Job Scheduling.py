class Solution: 
    def maxProfit(self, jobs):
        # Sort jobs by end time
        jobs.sort(key=lambda x: x[1])
        
        n = len(jobs)
        end_times = [job[1] for job in jobs]  # For binary search
        dp = [0] * n
        
        dp[0] = jobs[0][2]  # Profit of the first job
        
        import bisect
        
        for i in range(1, n):
            profit_including = jobs[i][2]
            
            # Find the last non-overlapping job using binary search
            idx = bisect.bisect_right(end_times, jobs[i][0]) - 1
            
            if idx != -1:
                profit_including += dp[idx]
            
            # Best profit at current job index
            dp[i] = max(dp[i-1], profit_including)
        
        return dp[-1]
