"""
Problem: Word Ladder
Difficulty: Hard
Source: LeetCode #127
Tags: graphs, bfs

Problem Statement:
    Given beginWord, endWord, and a wordList, find the length of the
    shortest transformation sequence from beginWord to endWord, such
    that only one letter can be changed at a time and each transformed
    word must exist in the wordList.

    Return 0 if no such transformation sequence exists.
    Note: beginWord does not need to be in wordList.

Examples:
    Example 1:
        Input:  beginWord = "hit", endWord = "cog",
                wordList = ["hot","dot","dog","lot","log","cog"]
        Output: 5
        Explanation: "hit" -> "hot" -> "dot" -> "dog" -> "cog"

    Example 2:
        Input:  beginWord = "hit", endWord = "cog",
                wordList = ["hot","dot","dog","lot","log"]
        Output: 0

Constraints:
    - 1 <= beginWord.length <= 10
    - endWord.length == beginWord.length
    - 1 <= wordList.length <= 5,000

Hint (read only if stuck):
    BFS where each word is a node. Two words are connected if they
    differ by exactly one letter. Use wildcard patterns (e.g., "h*t")
    for efficient neighbor lookup.
"""


def solution(beginWord: str, endWord: str, wordList: list[str]) -> int:
    # TODO: implement your solution here
    pass
