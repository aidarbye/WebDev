def no_teen_sum(a, b, c):
    def fix_teen(n):
        return n if n not in [13, 14, 17, 18, 19] else 0
    
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

print(no_teen_sum(1, 2, 3))  # Output: 6
print(no_teen_sum(2, 13, 1))  # Output: 3
print(no_teen_sum(2, 1, 14))  # Output: 3
