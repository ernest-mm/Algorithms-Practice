# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = int(1)
        indexOfZero = set()

        for i in range(len(nums)):
            if nums[i] == 0:
                indexOfZero.add(i)
            else:
                product *= nums[i]

        answer = []

        for i in range(len(nums)):
            if len(indexOfZero) == 0:
                answer.append(int(product * (nums[i] ** (-1))))
            elif i in indexOfZero and len(indexOfZero) == 1:
                answer.append(product)
            elif i not in indexOfZero and len(indexOfZero) == 1:
                answer.append(0)
            else:
                answer.append(0)

        return answer