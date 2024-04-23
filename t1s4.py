# روش اول: استفاده از حلقه‌های تو در تو
def pattern_one(n):
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            print(j, end=' ')
        print()

# روش دوم: استفاده از فهرست comprehensions
def pattern_two(n):
    for i in range(n, 0, -1):
        print(*range(n, 0, -1))

# روش سوم: استفاده از بازگشت معکوس برای رنج و قالب‌بندی رشته
def pattern_three(n):
    for i in range(n, 0, -1):
        print(' '.join(str(x) for x in range(n, 0, -1)))

# ورودی از کاربر گرفته می‌شود
number = int(input("عددی وارد کنید: "))

print("الگو 1:")
pattern_one(number)

print("الگو 2:")
pattern_two(number)

print("الگو 3:")
pattern_three(number)



#بخش دوم

def print_pattern(n):
    for i in range(n):
        for j in range(n, 0, -1):
            print(j, end=' ')
        print()

number = int(input("عددی وارد کنید: "))
print_pattern(number)