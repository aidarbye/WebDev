def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a.endswith(b) or b.endswith(a)

print(end_other('Hiabc', 'abc'))    # Output: True
print(end_other('AbC', 'HiaBc'))     # Output: True
print(end_other('abc', 'abXabc'))    # Output: True
