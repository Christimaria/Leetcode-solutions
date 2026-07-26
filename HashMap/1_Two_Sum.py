"""
LeetCode 1 - Two Sum

Concept:
Hash Map

Problem:
Given an array of integers nums and an integer target,
return the indices of the two numbers such that they add up to target.

Approach:
1. Create an empty dictionary.
2. Iterate through the array.
3. Compute the complement:
       need = target - nums[i]
4. If the complement already exists in the dictionary,
   return its index and the current index.
5. Otherwise, store the current number and its index.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""

class Solution(object):
    def twoSum(self, nums, target):

        seen = {}

        for i in range(len(nums)):

            need = target - nums[i]

            if need in seen:
                return [seen[need], i]

            seen[nums[i]] = i
