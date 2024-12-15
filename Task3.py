def second_largest(nums):
    unique_nums = list(set(nums))
    unique_nums.sort(reverse=True)
    return unique_nums[1] if len(unique_nums) > 1 else None

print(second_largest([10, 20, 4, 45, 99]))
