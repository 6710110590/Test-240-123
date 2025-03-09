def Funny_string(s):
    original_diffs = []
    for i in range(1, len(s)):
        original_diffs.append(abs(ord(s[i]) - ord(s[i-1])))
    
    reversed_s = s[::-1]
    reversed_diffs = []
    for i in range(1, len(reversed_s)):
        reversed_diffs.append(abs(ord(reversed_s[i]) - ord(reversed_s[i-1])))
    
    return "Funny" if original_diffs == reversed_diffs else "Not Funny"