# Title: Add Binary
# Submission ID: 1323524378
# Status: Accepted
# Date: 2024-07-17 01:10:27 UTC

class Solution(object):
    def addBinary(self,a,b):
        result = ""
        carry = 0

        if len(a) > len(b):
            b = "0"*(len(a) - len(b)) + b
        else:
            a = "0"*(len(b) - len(a)) + a

        for i in range(len(a)-1, -1, -1):
            current_sum = int(a[i]) + int(b[i]) + carry
            
            if current_sum == 0:
                result = "0" + result
                carry = 0
            
            elif current_sum == 1:
                result = "1" + result
                carry = 0

            elif current_sum == 2:
                result = "0" + result
                carry = 1

            else:
                result = "1" + result
                carry = 1

        if carry == 1:
            result = "1" + result

        return result