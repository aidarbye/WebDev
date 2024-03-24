def lucky_sum(a, b, c):
    if a == 13:
        return 0
    elif b == 13:
        return a
    elif c == 13:
        return a + b
    else:
        return a + b + c

print(lucky_sum(1, 2, 3))   # Output: 6
print(lucky_sum(1, 2, 13))  # Output: 3
print(lucky_sum(1, 13, 3))  # Output: 1
