"""
Problem: Brackets
Difficulty: Medium
Source: Codility Lesson 7
Tags: stacks, strings

Problem Statement:
    A string S consisting of N characters is considered to be properly nested
    if any of the following conditions is true:
        - S is empty
        - S has the form "(U)" or "[U]" or "{U}" where U is a properly nested
          string
        - S has the form "VW" where V and W are properly nested strings

    Given a string S consisting of N characters, return 1 if S is properly
    nested and 0 otherwise.

Examples:
    Example 1:
        Input:  S = "{[()()]}"
        Output: 1

    Example 2:
        Input:  S = "([)()]"
        Output: 0

Constraints:
    - 0 <= N <= 200,000
    - string S consists only of the characters '(', ')', '[', ']', '{', '}'

Hint (read only if stuck):
    Push opening brackets onto a stack. When encountering a closing bracket,
    check that the top of the stack is the matching opening bracket.
"""


def solution(S: str) -> int:
    # TODO: implement your solution here
    pass
