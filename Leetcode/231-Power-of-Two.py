"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:

Input: n = 3
Output: false
 
Constraints:

-231 <= n <= 231 - 1
 
Follow up: Could you solve it without loops/recursion?
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
            
        binary_n = bin(n)[2:]

        power_of_ten = len(binary_n) - 1
        binary_n = int(binary_n)
        
        remainder = binary_n % (10**power_of_ten)

        
        return remainder == 0
        
