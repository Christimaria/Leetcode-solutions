# ---------------------------------------------------------
# 35. Search Insert Position
#
# Idea:
# - Use Binary Search on the sorted array.
# - If target is found, return its index.
# - If target is not found, keep shrinking the search space.
# - When the loop ends (left > right):
#     right -> last element smaller than target
#     left  -> correct insertion position
#
# Example:
# nums = [1,3,5,6], target = 2
#
# End of loop:
# left = 1, right = 0
#
# Insert 2 at index 1 -> [1,2,3,5,6]
#
# Time Complexity : O(log n)
# Space Complexity: O(1)
# ---------------------------------------------------------
class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return left
