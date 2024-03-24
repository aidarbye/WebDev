def make_bricks(small, big, goal):
    return goal % 5 <= small and goal - big * 5 <= small

print(make_bricks(3, 1, 8))   # Output: True
print(make_bricks(3, 1, 9))   # Output: False
print(make_bricks(3, 2, 10))  # Output: True
