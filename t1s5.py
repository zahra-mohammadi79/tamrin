# روش اول: استفاده از حلقه‌های تو در تو
def two_sum_one(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False

# روش دوم: استفاده از مجموعه برای ذخیره عناصر دیده شده
def two_sum_two(nums, target):
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False

# روش سوم: استفاده از مرتب‌سازی و دو نشانگر
def two_sum_three(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return False

# ورودی از کاربر گرفته می‌شود
nums = list(map(int, input("آرایه را وارد کنید (اعداد را با فاصله جدا کنید): ").split()))
target = int(input("مقدار هدف را وارد کنید: "))

print("روش 1:", two_sum_one(nums, target))
print("روش 2:", two_sum_two(nums, target))
print("روش 3:", two_sum_three(nums, target))