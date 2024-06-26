def lower_triangular(n):
    for i in range(1, n+1):
        for j in range(i):
            print('*', end=' ')
        print()


def upper_triangular(n):
    for i in range(0, n):
        for j in range(i, 5):
            print('*', end=' ')
        print()


def pyramid(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print("", end=" ")
        for k in range(1, i + 1):
            print("*", end=" ")
        print()


n = 5
print("Lower Triangular:")
lower_triangular(n)
print("\nUpper Triangular:")
upper_triangular(n)
print("\nPyramid:")
pyramid(n)
