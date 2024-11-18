# V00701557 CAMERON COLLINS

ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS = "0123456789"

def is_alpha(word):
    for char in word:
        if char not in ASCII_LOWERCASE and char not in ASCII_UPPERCASE:
            return False
    return True

def is_digit(s):
    for char in s:
        if char not in DECIMAL_DIGITS:
            return False
    return True

def to_lower(s):
    result = ""
    for char in s:
        if char in ASCII_UPPERCASE:
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def to_upper(s):
    result = ""
    for char in s:
        if char in ASCII_LOWERCASE:
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def find_chr(s, char):
    if len(char) != 1:
        return -1
    for index in range(len(s)):
        if s[index] == char:
            return index
    return -1

def find_str(s, substr):
    if substr == "":
        return 0  
    for i in range(len(s) - len(substr) + 1):
        match = True
        for j in range(len(substr)):
            if s[i + j] != substr[j]:
                match = False
                break
        if match:
            return i
    return -1

def replace_chr(s, old, new):
    if len(old) != 1 or len(new) != 1:
        return "" 
    result = ""
    for char in s:
        if char == old:
            result += new
        else:
            result += char
    return result

def replace_str(s, old, new):
    if old == "":
        result = new.join(s)
        return new + result + new  
    result = ""
    i = 0
    while i < len(s):
        if s[i:i+len(old)] == old:
            result += new
            i += len(old)  
        else:
            result += s[i]
            i += 1
    return result