# Title: Climbing Stairs
# Submission ID: 1327401755
# Status: Time Limit Exceeded
# Date: 2024-07-20 15:03:26 UTC

class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


