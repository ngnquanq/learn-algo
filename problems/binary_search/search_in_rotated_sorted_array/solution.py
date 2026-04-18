"""
Problem: Search in Rotated Sorted Array
Difficulty: Medium
Source: LeetCode #33
Tags: binary-search, arrays

Problem Statement:
    An integer array nums sorted in ascending order was rotated at some
    pivot. Given the rotated array and a target value, return the index
    of target, or -1 if not found.

    You must write an algorithm with O(log n) runtime complexity.
    All values are unique.

Examples:
    Example 1:
        Input:  nums = [4,5,6,7,0,1,2], target = 0
        Output: 4

    Example 2:
        Input:  nums = [4,5,6,7,0,1,2], target = 3
        Output: -1

Constraints:
    - 1 <= N <= 5,000
    - All values are unique
    - Must be O(log n)

Hint (read only if stuck):
    At each step of binary search, one half is always sorted.
    Determine which half is sorted, then check if the target
    falls within that sorted half.
"""


def solution(nums: list[int], target: int) -> int:
    if not nums:
        return -1
        
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Target found
        if nums[mid] == target:
            return mid
            
        # Check if the left half is strictly sorted
        if nums[left] <= nums[mid]:
            # Check if the target falls within the sorted left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Target is in the left half
            else:
                left = mid + 1   # Target is in the right half
        # If the left half isn't sorted, the right half MUST be strictly sorted
        else:
            # Check if the target falls within the sorted right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # Target is in the right half
            else:
                right = mid - 1  # Target is in the left half

    return -1
