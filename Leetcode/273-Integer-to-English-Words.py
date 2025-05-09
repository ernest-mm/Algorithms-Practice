"""
TO ANYONE WHO MIGHT BE READING THIS:
  THIS CODE PASSES ALL THE TEST CASES BUT IT'S BADLY WRITTEN.
  
PROBLEM:
Convert a non-negative integer num to its English words representation.

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

Constraints:

0 <= num <= 231 - 1
"""

class Solution:
    def numberToWords(self, num: int) -> str:
        key_nums = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred"
        }

        if num == 0:
            return key_nums[0]

        def str_three_digits(three_digits_num: int) -> str:
            if three_digits_num == 0:
                return None
            
            if three_digits_num == 100:
                return key_nums[1] + " " + key_nums[three_digits_num]
            
            elif three_digits_num in key_nums:
                return key_nums[three_digits_num]
            
            str_num = str(three_digits_num)

            if three_digits_num < 100:
                if three_digits_num in key_nums:
                    return key_nums[three_digits_num]
                    
                tens = int(str_num[0]) * 10
                units = int(str_num[1])
                if units != 0:
                    result = key_nums[tens] + ' ' + key_nums[units]
                else:
                    result = key_nums[tens]
                return result
            
            else:
                hundreds_unit = int(str_num[0])
                tens_and_units = int(str_num[1]+str_num[2])
                if tens_and_units in key_nums:
                    if tens_and_units != 0:
                        result = (
                            key_nums[hundreds_unit] + ' ' + 
                            key_nums[100] + ' ' +
                            key_nums[tens_and_units]
                        )
                    else:
                        result = (
                            key_nums[hundreds_unit] + ' ' + 
                            key_nums[100]
                        )

                    return result
                
                else:
                    tens = int(str_num[1]) * 10
                    if tens != 0:
                        result = (
                            key_nums[hundreds_unit] + ' ' + 
                            key_nums[100] + ' ' +
                            key_nums[tens]
                        )
                    else:
                        result = (
                            key_nums[hundreds_unit] + ' ' + 
                            key_nums[100]
                        )

                    units = int(str_num[2])

                    if units != 0:
                        result += ' ' + key_nums[units]

                    return result

        place_values = ['', ' Thousand', ' Million', ' Billion']
        place_value_index = 0

        result_list = []

        while num > 0:
            three_digits = num % 1000
            three_digits_str = str_three_digits(three_digits)
            if three_digits_str is not None:
                three_digits_str += place_values[place_value_index]
                result_list.append(three_digits_str)

            num = num // 1000
            place_value_index += 1

        result = ''

        result_list = result_list[::-1]

        for i in range(len(result_list)):
            if i != 0:
                result += " " + result_list[i]
            else:
                result += result_list[i]

        return result
