"""Let’s print a triangle made of asterisks (‘*’) separated by spaces. The triangle
should consist of n rows, where n is a given positive integer, and consecutive rows should
contain 1, 2, . . . , n asterisks. """


def solution(n):
    for i in range(1, n + 1):
        for j in range(i):
            print('*', end="")
        print('\n')


def main():
    print(solution(10))


if __name__ == "__main__":
    main()
