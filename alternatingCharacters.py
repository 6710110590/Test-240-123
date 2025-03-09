def alternating_characters(s):
    if len(s) < 2:
        return 0
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            deletions += 1
    return deletions