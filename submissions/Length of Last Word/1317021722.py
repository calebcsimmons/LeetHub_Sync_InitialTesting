# Title: Length of Last Word
# Submission ID: 1317021722
# Status: Accepted
# Date: 2024-07-11 02:08:14 UTC

class Solution(object):
    def lengthOfLastWord(self, string):

        words = string.split() # Auto splits string into list of words and removes trailing spaces
        if not words: # If words list is empty
            return 0
        return len(words[-1])
        