def love6(a, b):
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6

print(love6(6, 4))  # Output: True
print(love6(4, 5))  # Output: False
print(love6(1, 5))  # Output: True
