def sum67(nums):
    total = 0
    ignore = False
    for num in nums:
        if num == 6:
            ignore = True
        elif num == 7 and ignore:
            ignore = False
        elif not ignore:
            total += num
    return total

print(sum67([1, 2, 2]))  # Output: 5
print(sum67([1, 2, 2, 6, 99, 99, 7]))  # Output: 5
print(sum67([1, 1, 6, 7, 2]))  # Output: 4
