# روش اول: استفاده از حلقه‌های تو در تو
def pattern_one(n):
    for i in range(1, n + 1):
        for j in range(4):
            print(i, end=' ')
        print()

# روش دوم: استفاده از فهرست comprehensions
def pattern_two(n):
    for i in range(1, n + 1):
        print(*[i]*4)

# روش سوم: استفاده از قالب‌بندی رشته
def pattern_three(n):
    for i in range(1, n + 1):
        print(f"{i} {i} {i} {i}")

# ورودی از کاربر گرفته می‌شود
number = int(input("عددی وارد کنید: "))

print("الگو 1:")
pattern_one(number)

print("الگو 2:")
pattern_two(number)

print("الگو 3:")
pattern_three(number)



#بخش دوم سوال

def print_pattern(n):
    for i in range(1, n + 1):
        print((str(i) + ' ') * 3)

number = int(input("عددی وارد کنید: "))
print_pattern(number)