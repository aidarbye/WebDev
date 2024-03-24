def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10

print(makes10(9, 10))  # Output: True
print(makes10(9, 9))   # Output: False
print(makes10(1, 9))   # Output: True
