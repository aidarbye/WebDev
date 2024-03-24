def power(a, n):
    if n == 0:
        return 1
    result = 1
    for _ in range(n):
        result *= a
    return result

a, n = map(float, input().split())
print(power(a, int(n)))