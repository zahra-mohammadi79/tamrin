# روش اول: استفاده از دو نشانگر
def is_subsequence_one(arr, sub_arr):
    arr_pointer = 0
    sub_arr_pointer = 0

    while arr_pointer < len(arr) and sub_arr_pointer < len(sub_arr):
        if arr[arr_pointer] == sub_arr[sub_arr_pointer]:
            sub_arr_pointer += 1
        arr_pointer += 1
    
    return sub_arr_pointer == len(sub_arr)

# روش دوم: استفاده از برش لیست
def is_subsequence_two(arr, sub_arr):
    if not sub_arr:
        return True
    if not arr:
        return False
    if arr[0] == sub_arr[0]:
        return is_subsequence_two(arr[1:], sub_arr[1:])
    else:
        return is_subsequence_two(arr[1:], sub_arr)

# روش سوم: استفاده از تابع داخلی all() و comprehensions لیست
def is_subsequence_three(arr, sub_arr):
    return all(x in arr for x in sub_arr)

# ورودی از کاربر گرفته می‌شود
arr = list(map(int, input("آرایه اصلی را وارد کنید (اعداد را با فاصله جدا کنید): ").split()))
sub_arr = list(map(int, input("آرایه زیرمجموعه را وارد کنید (اعداد را با فاصله جدا کنید): ").split()))

print("روش 1:", is_subsequence_one(arr, sub_arr))
print("روش 2:", is_subsequence_two(arr, sub_arr))
print("روش 3:", is_subsequence_three(arr, sub_arr))