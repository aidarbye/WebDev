import math

x = int(input())

divisors = 0

for i in range(1, int(math.sqrt(x)) + 1):
    if x % i == 0:
        divisors += 2

if int(math.sqrt(x)) ** 2 == x:
    divisors -= 1

print(divisors)