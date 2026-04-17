"""
Problem: Genomic Range Query
Difficulty: Medium
Source: Codility Lesson 5
Tags: prefix-sums, string

Problem Statement:
    A DNA sequence is given as a non-empty string S consisting of characters
    A, C, G and T. Each nucleotide has an impact factor:
        A = 1, C = 2, G = 3, T = 4

    You are given M queries, each defined by two integers P[i] and Q[i],
    representing a range in string S (0-indexed). For each query, find the
    minimal impact factor of nucleotides contained in the range S[P[i]..Q[i]].

Examples:
    Example 1:
        Input:  S = "CAGCCTA", P = [2, 5, 0], Q = [4, 5, 6]
        Output: [2, 4, 1]

        Explanation:
            Query 0: S[2..4] = "GCC" -> min impact = C = 2
            Query 1: S[5..5] = "T"   -> min impact = T = 4
            Query 2: S[0..6] = "CAGCCTA" -> min impact = A = 1

Constraints:
    - N is an integer within the range [1 .. 100,000]
    - M is an integer within the range [1 .. 50,000]
    - each element of arrays P and Q is an integer within the range [0 .. N-1]
    - P[i] <= Q[i]

Hint (read only if stuck):
    Build prefix sums for each nucleotide type (A, C, G, T). For each query,
    check if any A exists in the range (cheapest), then C, then G, else T.
"""


def solution(S: str, P: list[int], Q: list[int]) -> list[int]:
    # TODO: implement your solution here
    pass
