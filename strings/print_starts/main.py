n = 4
x = 1
char = "*"

while n > 0:
    i = 0
    print(" " * n, end=' ')
    while i < x:
        print(char, end=' ')
        i += 1
    print(" ")
    x += 1
    n -= 1

#    *
#   * *
#  * * *
# * * * *
