"""
LeetCode 189 - Rotate Array

Difficulty:
Medium

Concept:
Array Manipulation

Problem:
Rotate the array to the right by k steps.

Approach                        	Time	  Space
Brute Force (rotate one by one)	 O(n × k)	 O(1)
Extra Array                    	 O(n)	     O(n)
Reverse Method (Optimal)	       O(n)     O(1)

Intuition:
Instead of shifting one element at a time,
reverse different parts of the array.

Approach:
1. Reverse the entire array.
2. Reverse the first k elements.
3. Reverse the remaining elements.

Example:
[1,2,3,4,5,6,7]

↓

Reverse Entire Array

↓

Reverse First k

↓

Reverse Remaining

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern Learned:
Reverse Array
"""
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)      # Reverse whole array
        reverse(0, k - 1)      # Reverse first k elements
        reverse(k, n - 1)      # Reverse remaining elements
 
