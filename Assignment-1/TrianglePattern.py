def lower_triangular(n):
    print("Lower Triangular Pattern:")
    for i in range(n):
        for j in range(i + 1):
            print('*', end=' ')
        print()
    print()


def upper_triangular(n):
    print("Upper Triangular Pattern:")
    for i in range(n):
        for j in range(n):
            if j >= i:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
    print()


def pyramid(n):
    print("Pyramid Pattern:")
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end=' ')
        for k in range(2 * i + 1):
            print('*', end=' ')
        print()
    print()


n = 5
lower_triangular(n)
upper_triangular(n)
pyramid(n)
