"""
LeetCode 217 - Contains Duplicate

Concept : Hash Set

Problem:
Determine whether any value appears at least twice in the array.

Approach:
1. Create an empty hash set.
2. Traverse the array.
3. If the current number already exists in the set,
   return True.
4. Otherwise add it to the set.
5. If traversal finishes, return False.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern Learned:
Hash Set
"""

class Solution(object):

    def containsDuplicate(self, nums):

        seen = set()

        for num in nums:

            # Duplicate found
            if num in seen:
                return True

            # Store current number
            seen.add(num)

        return False
