def make_chocolate(small, big, goal):
    max_big = goal // 5
    if max_big >= big:
        goal -= 5 * big
    else:
        goal -= 5 * max_big
        
    if goal <= small:
        return goal
    else:
        return -1

print(make_chocolate(4, 1, 9))   # Output: 4
print(make_chocolate(4, 1, 10))  # Output: -1
print(make_chocolate(4, 1, 7))   # Output: 2
