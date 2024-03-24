number = int(input())

for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
        print(i)
        break
else:
    print(number)