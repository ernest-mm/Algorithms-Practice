"""
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

The solution I came up with:

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        valueRecurrence = dict()
        for integer in nums:
            valueRecurrence[integer] = 0

        for integer in nums:
            valueRecurrence[integer] += 1

        valueRecList = sorted(valueRecurrence.items(), key=lambda item: item[1])
        
        result = []

        i = len(valueRecList) - 1

        while k > 0:
            result.append(valueRecList[i][0])
            i -= 1
            k -=1

        return result

Neetcode's Bucket Sort Solution https://www.youtube.com/watch?v=YPTqKIgVk-k
"""
            
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        frequency = [[] for i in range(len(nums)+1)]
        for integer in nums:
            count[integer] = 1 + count.get(integer, 0)
        
        for integer, i in count.items():
            frequency[i].append(integer)

        result = []

        for i in range(len(frequency)-1, 0, -1):
            for integer in frequency[i]:
                result.append(integer)
                if len(result) == k:
                    return result