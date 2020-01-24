"""The Fibonacci numbers form a sequence of integers defined recursively in the
following way. The first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two. The first few elements in this sequence are: 0,
1, 1, 2, 3, 5, 8, 13. Let’s write a program that prints all the Fibonacci numbers, not exceeding
a given integer n."""


def solution(a):
    l = len(a) - 1
    aux = []
    while l >= 0:
        aux += [a[l]]
        l -= 1
    return aux


def solution2(a):
    a.reverse()
    return a


def solution3(a):
    return a[::-1]


def solution4(a):
    n = len(a)
    for i in range(n // 2):
        k = n - i - 1
        a[i], a[k] = a[k], a[i]
    return a


def main():
    print(solution([1, 2, 3, 4, 5]))
    print(solution2([1, 2, 3, 4, 5]))
    print(solution3([1, 2, 3, 4, 5]))
    print(solution4([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()
