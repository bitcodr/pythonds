n = 12345

x = 0

while n > 0:
    remainder = int(n % 10)
    x *= 10
    x += remainder
    n = int(n / 10)

print(int(x))
