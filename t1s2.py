# روش اول
def pattern1(num):
    for i in range(num, 0, -1):
        print((str(i) + ' ') * 4)

# روش دوم
def pattern2(num):
    for i in range(num, 0, -1):
        for _ in range(4):
            print(i, end=' ')
        print()

# روش سوم
def pattern3(num):
    for i in range(num, 0, -1):
        print(' '.join([str(i)] * 4))

# دریافت ورودی از کاربر
num = int(input("عددی وارد کنید: "))

# فراخوانی هر تابع با عدد ورودی
pattern1(num)
print("\n")
pattern2(num)
print("\n")
pattern3(num)


#بخش دوم سوال


def print_pattern(num):
    for i in range(num, 0, -1):
        print((str(i) + ' ') * 4)

# ورودی از کاربر گرفته می‌شود
num = int(input("عددی وارد کنید: "))

# تابع برای چاپ الگو فراخوانی می‌شود
print_pattern(num)