def is_palindrome_method1(s):
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())
    return s == s[::-1]

# تست تابع
print(is_palindrome_method1("racecar"))  # True
print(is_palindrome_method1("hello"))    # False
print(is_palindrome_method1("A man, a plan, a canal, Panama"))  # True



#راه حل دوم

def is_palindrome_method2(s):
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# تست تابع
print(is_palindrome_method2("racecar"))  # True
print(is_palindrome_method2("hello"))    # False
print(is_palindrome_method2("A man, a plan, a canal, Panama"))  # True