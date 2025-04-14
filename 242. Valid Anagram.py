'''
Step-by-step Approach:
Length Check: If s and t have different lengths, they can't be anagrams.

Frequency Count: Count how many times each character appears in both strings.

Comparison: Compare the two frequency dictionaries or use a built-in data structure.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        from collections import Counter
        return Counter(s) == Counter(t)
