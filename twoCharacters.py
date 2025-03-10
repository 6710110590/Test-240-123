def alternate_two_characters(s):
    max_length = 0
    unique_chars = list(set(s))
    
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1, char2 = unique_chars[i], unique_chars[j]
            temp = [c for c in s if c == char1 or c == char2]
            
            is_alternating = True
            for k in range(len(temp) - 1):
                if temp[k] == temp[k + 1]:
                    is_alternating = False
                    break
            
            if is_alternating:
                max_length = max(max_length, len(temp))
    
    return max_length