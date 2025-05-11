"""
Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_digits = []
        x_copy = x

        while x_copy > 0:
            remainder = x_copy % 10
            reversed_digits.append(remainder)
            x_copy = x_copy // 10

        ten_power = len(reversed_digits) - 1
        reversed_num = 0

        for digit in reversed_digits:
            reversed_num += digit * (10**ten_power)
            ten_power -= 1

        return reversed_num == x
            
        
