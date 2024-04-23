def are_anagrams_method1(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

# تست تابع
string1 = "listen"
string2 = "silent"
print(are_anagrams_method1(string1, string2))  # Output: True

string3 = "hello"
string4 = "world"
print(are_anagrams_method1(string3, string4))  # Output: False


#روش دوم 


def are_anagrams_method2(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return False
    
    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False
    
    return all(value == 0 for value in char_count.values())

# تست تابع
string1 = "listen"
string2 = "silent"
print(are_anagrams_method2(string1, string2))  # Output: True

string3 = "hello"
string4 = "world"
print(are_anagrams_method2(string3, string4))  # Output: False