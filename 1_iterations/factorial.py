"""We are given some positive integer n. Let’s compute the factorial of n and assign
it to the variable factorial. The factorial of n is n! = 1 · 2 · . . . · n. We can obtain it by
starting with 1 and multiplying it by all the integers from 1 to n."""


def solution(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


def main():
    print(solution(5))


if __name__ == "__main__":
    main()
