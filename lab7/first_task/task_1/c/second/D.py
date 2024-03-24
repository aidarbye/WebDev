N = int(input())

is_power_of_two = False
power_of_two = 1

while power_of_two <= N:
    if power_of_two == N:
        is_power_of_two = True
        break
    power_of_two *= 2

if is_power_of_two:
    print("YES")
else:
    print("NO")