def near_ten(num):
    return num % 10 in [0, 1, 2, 8, 9]

print(near_ten(12))  # Output: True
print(near_ten(17))  # Output: False
print(near_ten(19))  # Output: True
