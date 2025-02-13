"""
You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.
Return the minimum number of steps to make t an anagram of s.
An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Example 2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

Example 3:
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
"""

from collections import defaultdict


class Solution:
    def minSteps(self, s: str, t: str) -> int:

        # create hashmap for s
        s_map = {}
        for c in s:
            if c in s_map:
                s_map[c] += 1
            else:
                s_map[c] = 1

        # create hashmap for t
        t_map = {}
        for c in t:
            if c in t_map:
                t_map[c] += 1
            else:
                t_map[c] = 1
        # print(t_map, s_map)
        # compare them both
        min_steps = 0
        for k in t_map:
            if k in s_map:
                if t_map[k] > s_map[k]:
                    min_steps += abs(s_map[k] - t_map[k])
            else:
                min_steps += t_map[k]

        return min_steps

    def minStepsDefaultDict(self, s: str, t: str) -> int:

        # Count frequency of each character in s
        freq_s = defaultdict(int)
        for char in s:
            freq_s[char] += 1

        # Count frequency of each character in t
        freq_t = defaultdict(int)
        for char in t:
            freq_t[char] += 1

        # Calculate the difference in frequencies
        steps = 0
        for char in freq_s:
            if freq_s[char] > freq_t[char]:
                steps += freq_s[char] - freq_t[char]

        return steps


# Test cases
s = Solution()
print(s.minSteps("bab", "aba"))  # Output: 1
print(s.minStepsDefaultDict("leetcode", "practice"))  # Output: 5
print(s.minSteps("anagram", "mangaar"))  # Output: 0
