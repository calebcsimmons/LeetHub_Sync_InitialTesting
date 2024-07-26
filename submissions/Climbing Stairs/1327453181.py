# Title: Climbing Stairs
# Submission ID: 1327453181
# Status: Accepted
# Date: 2024-07-20 15:30:36 UTC

class Solution(object):
    def climbStairs(self, n, dic = None):
        # Recursive Function: f(n) = f(n-1) + f(n-2)
        
        if dic is None:
            dic = {}

        if n in dic:
            return dic[n]

        if n <= 2:
            return n
        
        dic[n] = self.climbStairs(n-1, dic) + self.climbStairs(n-2, dic)
        return dic[n]

        # Memoization
        # (Create dictionary to store values already calculated for recall later.
        # This improves the Time Complexity from O(2^n) to O(n)