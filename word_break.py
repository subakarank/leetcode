def wordBreak(s, wordDict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break

    return dp[n]

# Example usage:
s = "leetcode"
wordDict = {"leet", "code"}
print(wordBreak(s, wordDict))  # Output: True

s = "applepenapple"
wordDict = {"apple", "pen"}
print(wordBreak(s, wordDict))  # Output: True

s = "catsandog"
wordDict = {"cats", "dog", "sand", "and", "cat"}
print(wordBreak(s, wordDict))  # Output: False
