# Title: Plus One
# Submission ID: 1321257577
# Status: Accepted
# Date: 2024-07-15 00:07:13 UTC

class Solution(object):
    def plusOne(self, digits):
        n = len(digits)

        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        return [1] + [0] * n
        