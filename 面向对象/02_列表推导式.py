a = [x for x in range(10)]
print(a)

a = [x for x in range(10) if x % 2 == 0]
print(a)

a = [(x, y) for x in range(3) for y in range(3)]
print(a)
