# Title: Climbing Stairs
# Submission ID: 1327406853
# Status: Accepted
# Date: 2024-07-20 15:05:58 UTC

class Solution(object):
    def __init__(self):
        self.memo = {}
    
    def climbStairs(self, n):
        if n in self.memo:
            return self.memo[n]
        if n <= 2:
            return n
        
        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]