'''
https://leetcode.com/problems/valid-word-abbreviation/description/
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths.
 The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.
'''

def valid_word_abbreviation(word, abbr):
    i, j = 0, 0
    n, m = len(word), len(abbr)
    
    while i < n and j < m:
        if abbr[j].isalpha():
            if abbr[j] != word[i]:
                return False
            i += 1
            j += 1
        else:
            if abbr[j] == '0':
                return False  # Leading zero is not allowed
            num = 0
            while j < m and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j += 1
            i += num
    
    return i == n and j == m

# Example usage
print(valid_word_abbreviation("internationalization", "i12iz4n"))  # Output: true
print(valid_word_abbreviation("apple", "a2e"))  # Output: false
