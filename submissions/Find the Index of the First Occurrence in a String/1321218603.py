# Title: Find the Index of the First Occurrence in a String
# Submission ID: 1321218603
# Status: Accepted
# Date: 2024-07-14 22:28:13 UTC

class Solution(object):
    def strStr(self, haystack, needle):
        if needle not in haystack:
            return -1

        return haystack.index(needle)
        