def count_hi(s):
    count = 0
    for i in range(len(s) - 1):
        if s[i:i+2] == 'hi':
            count += 1
    return count

print(count_hi('abc hi ho'))  # Output: 1
print(count_hi('ABChi hi'))   # Output: 2
print(count_hi('hihi'))       # Output: 2
