"""
 Problem :Given an array nums containing n distinct numbers in the range [0, n],
 return the only number in the range that is missing from the array.
 
 💡 Logic Explanation
 This solution uses a mathematical approach based on Gauss' Summation Formula.
 
 Calculate Expected Sum: 
 The sum of all consecutive integers from 0 to n can be found instantly using the formula:
 {Sum}=(n x (n+1))/2
 
 Calculate Actual Sum: 
 Sum up all the elements currently present in the input array nums.
 Find the Missing Number: Subtract the actual_sum from the expected_sum. 
 
 The difference is exactly the missing number because every other number contributes equally to both sums.
"""
 class Solution(object):
    def missingNumber(self, nums):
        
        # n is the count of numbers, representing the maximum range boundary [0, n]
        n = len(nums)

        # Gauss formula calculates the sum of all numbers from 0 to n
        # Uses integer division (//) to avoid floating-point issues
        expected_sum = n * (n + 1) // 2

        # Sum up all the numbers actually present in the given list
        actual_sum = sum(nums)

        # The difference between what we should have and what we actually have is the missing number
        return expected_sum - actual_sum
