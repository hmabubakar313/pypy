def is_palindrome(s: str) -> bool: 
    return s == s[::-1]


print(is_palindrome("raccar")) 