def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    max_length = 0
    left = 0 

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        print(char_set, left , right )
        max_length = max(max_length, right - left + 1 )
        print("max_length", max_length)
    return max_length

s = "abcabcbb"
print(lengthOfLongestSubstring(s))

