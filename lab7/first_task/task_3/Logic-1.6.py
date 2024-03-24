def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    else:
        return 1 <= n <= 10

print(in1to10(5, False))  # Output: True
print(in1to10(11, False)) # Output: False
print(in1to10(11, True))  # Output: True
