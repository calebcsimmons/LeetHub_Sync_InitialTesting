# Title: Remove Duplicates from Sorted Array
# Submission ID: 1321036976
# Status: Wrong Answer
# Date: 2024-07-14 17:50:59 UTC

class Solution(object):
    def removeDuplicates(self, nums):
        nums[:] = (set(nums))
        k = len(nums)
        return k
        
# 'set' removes duplicates from a list
# 'sorted' sorts a list in order
# nums[:] ensures that any references to the original list nums will see the updated contents, unlike nums = sorted(set(nums)), which would create a new list object.