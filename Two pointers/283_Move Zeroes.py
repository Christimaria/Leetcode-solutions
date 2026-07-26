"""
Problem:
Given an integer array nums,move all 0's to the end while maintaining the relative order of the non-zero elements.
Do this IN-PLACE.
Example:
nums = [0,1,0,3,12]
output:[1,3,12,0,0]
The question says Move the zeroes IN-PLACE
What does in-place mean?

It means Don't create another list
First Thought (Brute Force)
You might think: I'll make another list.
"""
new = []

for every number

if number isn't zero

add it

then add all zeros
"""
This works...BUT...It uses extra memory.

That's where Two Pointers comes in.

Read Pointer
"I'll inspect every element."

 Write Pointer
"Whenever you find a good (non-zero) element, tell me where to place it."

Now code will make sense 

Time: O(n) ✅ (we visit each element only once)
Space: O(1) ✅ (no extra array)
"""
class Solution:
    def moveZeroes(self, nums):
      
      #the first position available for a non-zero number is index 0.
        write = 0
      
      # Scans through every element in the array
        for read in range(len(nums)):
          
      # If the current element is not a zero
            if nums[read] != 0:
              
     # Swap the elements at the 'write' and 'read' positions
     # This moves the non-zero forward and pushes the zero backward
                nums[write], nums[read] = nums[read], nums[write]
              
     # Move the write pointer to the next available slot
                write += 1
