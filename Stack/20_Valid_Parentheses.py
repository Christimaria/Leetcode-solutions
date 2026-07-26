"""
LeetCode 20 - Valid Parentheses

Difficulty:
Easy

Concept:
Stack

Problem:
Determine whether the input string has valid matching brackets.

Approach:
1. Push every opening bracket onto the stack.
2. For every closing bracket:
   - If the stack is empty, return False.
   - Pop the top element and check if it matches.
3. At the end, the stack should be empty.s

A string containing brackets.
Example:
s = "()[]{}"

LeetCode calls
Solution().isValid("()[]{}")
Return
True if brackets are balanced.
False otherwise.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern Learned:
Stack
"""

class Solution(object):
    def isValid(self, s):

        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:

            if ch in "({[":
                stack.append(ch)

            else:

                if not stack:
                    return False

                top = stack.pop()

                if top != pairs[ch]:
                    return False

        return not stack
