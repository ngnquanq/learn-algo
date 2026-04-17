"""
Problem: Stone Wall
Difficulty: Medium
Source: Codility Lesson 7
Tags: stacks, greedy

Problem Statement:
    You are going to build a stone wall. The wall should have different
    heights at different points — given by array H of N positive integers.
    The wall is built using rectangular stone blocks.

    Find the minimum number of blocks needed to build the wall.

Examples:
    Example 1:
        Input:  H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
        Output: 7

Constraints:
    - 1 <= N <= 100,000
    - 1 <= H[i] <= 1,000,000,000

Hint (read only if stuck):
    Use a stack. When the current height is less than the stack top,
    pop (those blocks are done). When it's a new height not already
    on the stack, push it and count a new block.
"""


def solution(H: list[int]) -> int:
    # TODO: implement your solution here
    pass
