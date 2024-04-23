def generate_primes_method1(n):
    primes = []
    for num in range(2, n):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

# تست تابع
limit = 20
print(generate_primes_method1(limit))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]


#روش دوم


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes_method2(n):
    primes = [num for num in range(2, n) if is_prime(num)]
    return primes

# تست تابع
limit = 20
print(generate_primes_method2(limit))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]