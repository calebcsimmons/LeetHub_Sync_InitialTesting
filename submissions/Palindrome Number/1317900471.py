# Title: Palindrome Number
# Submission ID: 1317900471
# Status: Accepted
# Date: 2024-07-11 18:24:10 UTC

class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        if x == x[::-1]:
            return True
        return False
