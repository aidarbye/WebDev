def squirrel_play(temperature, is_summer):
    if is_summer:
        return 60 <= temperature <= 100
    else:
        return 60 <= temperature <= 90

print(squirrel_play(70, False)) # Output: True
print(squirrel_play(95, False)) # Output: False
print(squirrel_play(95, True))  # Output: True
