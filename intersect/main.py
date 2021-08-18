x = [7, 3, 7, 9, 2, 5, 1, 0]
y = [8, 3, 0, 1, 6]

m = {}

for i in x:
    m[i] = i

g = []

for i in y:
    if m.get(i) == i:
        g.append(i)

print(g)
