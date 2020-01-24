"""Let’s print a triangle made of asterisks (‘*’) separated by spaces and consisting
of n rows again, but this 3_time_complexity upside down, and make it symmetrical. Consecutive rows should
contain 2n − 1, 2n − 3, . . . , 3, 1 asterisks and should be indented by 0, 2, 4, . . . , 2(n − 1)
spaces. """


def solution(n):
    for i in range(n, 0, -1):
        print((' '*(n-i))+('*'*(2*i-1)))

def main():
    print(solution(10))


if __name__ == "__main__":
    main()
