def not_string(string):
    if string.startswith("not"):
        return string
    else:
        return "not " + string

# Test cases
print(not_string('candy'))   # Output: 'not candy'
print(not_string('x'))       # Output: 'not x'
print(not_string('not bad')) # Output: 'not bad'
