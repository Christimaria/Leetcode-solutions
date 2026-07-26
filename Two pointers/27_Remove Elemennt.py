'''
This is the same Two Pointer pattern as Move Zeroes. Instead of keeping non-zero elements, I'm keeping elements that are not equal to val.
'''
class Solution:
    def removeElement(self, nums, val):

        write = 0

        for read in range(len(nums)):

            if nums[read] != val:

                nums[write], nums[read] = nums[read], nums[write]

                write += 1

        return write
      """
In both problems, the write pointer has the same meaning:

"The next position where a valid element should be placed."

The only difference is what the problem asks us to do with it.

Move Zeroes: Use write to rearrange the array. No return.
Remove Element: Use write to rearrange the array and return its final value because it represents k. Return write.
