def reverse_words_method1(s):
    words = s.split()
    reversed_string = ' '.join(reversed(words))
    return reversed_string

# تست تابع
input_string = "hello world"
print(reverse_words_method1(input_string))  # Output: "world hello"


#روش دوم


def reverse_words_method2(s):
    def reverse_helper(s):
        words = s.split()
        if len(words) == 1:
            return s
        return reverse_helper(' '.join(words[1:])) + ' ' + words[0]
    
    return reverse_helper(s)

# تست تابع
input_string = "hello world"
print(reverse_words_method2(input_string))  # Output: "world hello"