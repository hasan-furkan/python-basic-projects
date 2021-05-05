start = 1
fibonacci = [start]
while fibonacci[-1] < 55:
    fibonacci.append(sum(fibonacci[-2:]))
print(fibonacci)