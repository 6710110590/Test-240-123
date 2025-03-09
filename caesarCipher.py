def caesar_cipher(s, k):
    result = []
    for char in s:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result.append(chr((ord(char) - shift + k) % 26 + shift))
        else:
            result.append(char)
    return ''.join(result)
