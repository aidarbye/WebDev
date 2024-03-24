def sorta_sum(a, b):
    if 10 <= a + b <= 19:
        return 20
    else:
        return a + b

print(sorta_sum(3, 4))   # Output: 7
print(sorta_sum(9, 4))   # Output: 20
print(sorta_sum(10, 11)) # Output: 21
