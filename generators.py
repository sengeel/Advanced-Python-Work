def topten():
    n = 1

    while n <= 10:
        sq = n * n
        yield sq
        n += 1

values = topten()

for i in values:
    print(i)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib))
# Output: 0 1 1 2 3 5 8 13 21 34

