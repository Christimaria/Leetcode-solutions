# ---------------------------------------------------------
# 69. Sqrt(x)
#
# Idea:
# - Binary search on the answer (0 to x).
# - Compare mid * mid with x.
# - If equal, return mid.
# - If mid * mid < x, search the right half.
# - If mid * mid > x, search the left half.
# - If no perfect square exists, return right.
#
# Why return right?
# - At the end of the loop:
#     left  -> first number whose square is greater than x
#     right -> largest number whose square is <= x
#
# Time Complexity : O(log x)
# Space Complexity: O(1)
# ---------------------------------------------------------
class Solution(object):
    def mySqrt(self, x):
        left=0
        right=x
        while left <= right:
            mid=(left + right)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                left=mid+1
            else :
                right=mid-1
        return right


       
            
            
           
        
